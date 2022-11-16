from copy import deepcopy
from exceptions import PathError
from pathlib import Path
import shutil

FILES_EXTENTIONS = {
    "Audio": [".mp3", ".aac", ".ac3", ".wav", ".amr", ".ogg"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
    "Images": [".jpg", ".jpeg", ".png", ".svg", ".gif"],
    "Documents": [".doc", ".docx", ".txt", ".pdf", ".xls", ".xlsx", ".pptx", ".rtf"],
    "Books": [".fb2", ".epub", ".mobi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

all_files = {
    'Audio': [],
    'Video': [],
    'Images': [],
    'Documents': [],
    'Archives': [],
    'Books': [],
    'Other': []
}

known_types = set()

unknown_types = set()

initial_path: Path | None = None


def check_path(path_to_folder):
    path = Path(path_to_folder)

    if path.exists():
        if path.is_dir():
            return path
        else:
            raise PathError(f'Path {path.absolute()} is not a directory')

    else:
        raise PathError(f'Path {path.absolute()} is not exist')


def delete_empty(path):
    if path.is_dir():
        for element in path.iterdir():
            if element.is_dir():
                delete_empty(element)
                try:
                    element.rmdir()
                except OSError:
                    pass


def normalize(file_name):

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}

    for cyr, trans in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(cyr)] = trans
        TRANS[ord(cyr.upper())] = trans.upper()

    for sign in "!#$%&' \(\)\+,-;=@[]^`\{\}~.№":
        file_name = file_name.replace(sign, "_")

    new_file_name = file_name.translate(TRANS)

    return new_file_name


def run_sorting(path_to_folder):
    global initial_path

    path = check_path(path_to_folder)
    initial_path = deepcopy(path)

    sort_folder(path)
    delete_empty(path)

    return f"Я відсортував усі файли в папці {path}\n"\
        f"Я зміг розсортувати наступні типи файлів: {known_types}\n"\
        f"А ці типи фалів я нажаль не знаю: {unknown_types} \n"


def sort_folder(path):

    if path.is_dir():
        if path.name in ['Music', 'Video', 'Images', 'Documents', 'Archives', 'Books']:
            for element in path.iterdir():
                sort_folder(element)

        else:
            try:
                new_name = path.parent.joinpath(normalize(path.name))
                path.rename(new_name)
                for element in new_name.iterdir():
                    sort_folder(element)

            except PermissionError:
                for element in path.iterdir():
                    sort_folder(element)

# if path is file:
    else:
        sort_files(path)


def sort_files(path):
    suffix = path.suffix.lower()
    file_name = path.stem

    for file_type, extentions in FILES_EXTENTIONS.items():
        if suffix in extentions:
            destination_folder = initial_path.joinpath(file_type)
            destination_folder.mkdir(exist_ok=True)

            new_file_name = destination_folder.joinpath(
                normalize(file_name) + suffix)

            index = 0
            while True:
                try:
                    path.rename(new_file_name)
                    break

                except FileExistsError:
                    index += 1
                    new_file_name = destination_folder.joinpath(
                        normalize(file_name) + "_" + str(index) + suffix)

            all_files[file_type].append(new_file_name.name)
            known_types.add(suffix)

            if file_type == 'Archives':
                try:
                    shutil.unpack_archive(
                        new_file_name, destination_folder.joinpath(new_file_name.stem))
                except shutil.ReadError:
                    pass

            return

    all_files['Other'].append(file_name)
    unknown_types.add(suffix)
