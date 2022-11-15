import pickle


class Note:
    def __init__(self, note_text):
        self.note_text = note_text
        self.note_tags = set()


class Notes:
    notes_iter = 0

    def __init__(self):
        self.notes = {}
        self.load_notes_from_file()

    def add_note(self, note_text):
        self.notes[self.notes_iter] = Note(note_text)
        self.notes_iter += 1

    def delete_note(self, note_id):
        self.notes.pop(note_id)

    def get_notes(self):
        for key, value in self.notes.items():
            yield key, value

    def add_tags(self, note_id, tags):
        for tag in tags:
            self.notes[note_id].note_tags.add(tag)

    def note_exist_by_id(self, note_id):
        return note_id in self.notes

    def edit_note(self, note_id, new_note_text):
        self.notes[note_id].note_text = new_note_text

    def search_notes(self, search_text):
        search_result = {}
        for key, value in self.notes.items():
            if search_text in value.note_text:
                search_result[key] = value
        return search_result

    def search_notes_by_tags(self, tags):
        search_result = {}
        for key, value in self.notes.items():
            for tag in tags:
                if tag in value.note_tags:
                    if tag not in search_result:
                        search_result[tag] = {}
                    search_result[tag][key] = value

        return search_result

    def sort_notes(self):
        return dict(sorted(self.notes.items(), key=lambda item: item[1].note_text))

    def save_notes_to_file(self):
        with open('notes.pickle', 'wb') as file:
            pickle.dump(self.notes, file)

    def load_notes_from_file(self):
        try:
            with open('notes.pickle', 'rb') as file:
                self.notes = pickle.load(file)

                if self.notes:
                    self.notes_iter = len(self.notes.keys())
        except FileNotFoundError:
            pass


user_notes = Notes()
