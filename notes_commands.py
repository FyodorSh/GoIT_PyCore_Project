from notes import user_notes
from decorator import input_error


def add_note(data):
    note_text = data
    user_notes.add_note(note_text)
    return "New note added"


def show_notes():
    result = ""
    for key, value in user_notes.get_notes():
        result += 20 * "-" + "\n"
        result += f"note id - {key}\n"
        result += f"note text - {value.note_text}\n"
        if value.note_tags:
            result += f"tags - {' '.join(tag for tag in value.note_tags)}\n"
    return result


@input_error
def add_tags(data):
    note_id, *tags = data.split(" ")

    note_id = int(note_id)

    if user_notes.note_exist_by_id(note_id):
        user_notes.add_tags(note_id, tags)
        return "Tags added"
    else:
        return f"Note with id [{note_id}] doesn't exist"


@input_error
def delete_note(data):
    note_id = int(data)

    if user_notes.note_exist_by_id(note_id):
        user_notes.delete_note(note_id)
        return f"Note [{note_id}] deleted"
    else:
        return f"Note with id [{note_id}] doesn't exist"


@input_error
def edit_note(data):
    note_id, *note_text_list = data.split(" ")
    note_id = int(note_id)
    note_text = " ".join(note_text_list)

    if user_notes.note_exist_by_id(note_id):
        user_notes.edit_note(note_id, note_text)
        return f"Note [{note_id}] edited"
    else:
        return f"Note with id [{note_id}] doesn't exist"


def search_notes(data):
    result = ""
    for key, value in user_notes.search_notes(data).items():
        result += 20 * "-" + "\n"
        result += f"note id - {key}\n"
        result += f"note text - {value.note_text}\n"
        if value.note_tags:
            result += f"tags - {' '.join(tag for tag in value.note_tags)}\n"
    return result
