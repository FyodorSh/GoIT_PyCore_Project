# from collections import UserDict


class Note:
    def __init__(self, note_text, tags=None):
        self.note_text = note_text
        self.note_tags = tags


class Notes:
    notes_iter = 0

    def __init__(self):
        self.notes = {}

    def add_note(self):
        note_text = input("Enter note text - ")
        note_tags = input("Enter note tags (use for separate ' ') - ").strip().split(sep=' ')
        self.notes[self.notes_iter] = Note(note_text, note_tags)
        self.notes_iter += 1

    def show_notes(self):
        for key, value in self.notes.items():
            print(20 * "-")
            print(f"note id - {key}")
            print(f"note text - {value.note_text}")
            print(f"tags - {' '.join(tag for tag in value.note_tags)}")
