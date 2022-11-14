from copy import deepcopy
from exceptions import PathError
from pathlib import Path
import shutil

audio = [".mp3", ".aac", ".ac3", ".wav", ".amr", ".ogg"]

video = [".mp4", ".mov", ".avi", ".mkv"]

image = [".jpg", ".jpeg", ".png", ".svg", ".gif"]

doc = [".doc", ".docx", ".txt", ".pdf", ".xls", ".xlsx", ".pptx", ".rtf"]

book = [".fb2", ".epub", ".mobi"]

archive = [".zip", ".rar", ".tar", ".gz"]

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

initial_path = None


def delete_empty(path):
    if path.is_dir():
        for element in path.iterdir():
            if element.is_dir():
                delete_empty(element)
                try:
                    element.rmdir()
                except OSError:
                    pass


def is_archive(file_path):
    return file_path.suffix.lower() in archive


def is_audio(file_path):
    return file_path.suffix.lower() in audio


def is_book(file_path):
    return file_path.suffix.lower() in book


def is_doc(file_path):
    return file_path.suffix.lower() in doc


def is_image(file_path):
    return file_path.suffix.lower() in image


def is_video(file_path):
    return file_path.suffix.lower() in video


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


def check_path(path_to_folder):
    path = Path(path_to_folder)

    if path.exists():
        if path.is_dir():
            return path
        else:
            raise PathError(f'Path {path.absolute()} is not a directory')

    else:
        raise PathError(f'Path {path.absolute()} is not exist')


def run_sorting(path_to_folder):
    global initial_path

    path = check_path(path_to_folder)
    initial_path = deepcopy(path)

    sort_files(path)
    delete_empty(path)

    return f"Я відсортував усі файлив папці {path}\n"\
        f"Я зміг розсортувати наступні типи файлів: {known_types}\n"\
        f"А ці типи фалів я нажаль не знаю: {unknown_types} \n"


def sort_files(path):

    if path.is_dir():
        if path.name in ['Music', 'Video', 'Images', 'Documents', 'Archive', 'Books']:
            for element in path.iterdir():
                sort_files(element)

        else:
            try:
                new_name = path.parent.joinpath(normalize(path.name))
                path.rename(new_name)
                for element in new_name.iterdir():
                    sort_files(element)

            except PermissionError:
                for element in path.iterdir():
                    sort_files(element)

# if path is file:
    else:
        suffix = path.suffix.lower()

        if is_audio(path):

            audio_path = initial_path.joinpath("Audio")
            audio_path.mkdir(exist_ok=True)

            new_name = audio_path.joinpath(
                normalize(path.stem) + suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = audio_path.joinpath(
                    normalize(path.stem) + '(1)' + suffix)
                path.rename(new_name)

            all_files['Audio'].append(new_name.name)
            known_types.add(suffix)

        elif is_image(path):

            images_path = initial_path.joinpath("Images")
            images_path.mkdir(exist_ok=True)

            new_name = images_path.joinpath(normalize(path.stem) + suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = images_path.joinpath(
                    normalize(path.stem) + '(1)' + suffix)
                path.rename(new_name)

            all_files['Images'].append(new_name.name)
            known_types.add(suffix)

        elif is_video(path):

            video_path = initial_path.joinpath("Video")
            video_path.mkdir(exist_ok=True)

            new_name = video_path.joinpath(
                normalize(path.stem) + suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = video_path.joinpath(
                    normalize(path.stem) + '(1)' + suffix)
                path.rename(new_name)

            all_files['Video'].append(new_name.name)
            known_types.add(suffix)

        elif is_doc(path):

            doc_path = initial_path.joinpath("Documents")
            doc_path.mkdir(exist_ok=True)

            new_name = doc_path.joinpath(
                normalize(path.stem) + suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = doc_path.joinpath(
                    normalize(path.stem) + '(1)' + suffix)
                path.rename(new_name)

            all_files['Documents'].append(new_name.name)
            known_types.add(suffix)

        elif is_book(path):

            book_path = initial_path.joinpath("Books")
            book_path.mkdir(exist_ok=True)

            new_name = book_path.joinpath(normalize(path.stem) + suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = doc_path.joinpath(
                    normalize(path.stem) + '(1)' + suffix)
                path.rename(new_name)

            all_files['Books'].append(new_name.name)
            known_types.add(suffix)

        elif is_archive(path):

            archive_path = initial_path.joinpath("Archives")
            archive_path.mkdir(exist_ok=True)

            try:
                new_name = archive_path.joinpath(
                    normalize(path.stem) + suffix)
                path.rename(new_name)

            except FileExistsError:
                new_name = archive_path.joinpath(
                    normalize(path.stem) + '(1)' + suffix)
                path.rename(new_name)

            all_files['Archives'].append(new_name.name)
            known_types.add(suffix)

            try:
                shutil.unpack_archive(
                    new_name, archive_path.joinpath(new_name.stem))

            except shutil.ReadError:
                pass

        else:
            new_name = path.parent.joinpath(normalize(path.stem) + suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = path.parent.joinpath(
                    normalize(path.stem) + '(1)' + suffix)
                path.rename(new_name)

            all_files['Other'].append(new_name.name)
            unknown_types.add(suffix)
