from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Email(Field):
    pass


class Birthday(Field):
    pass


class Note:
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
