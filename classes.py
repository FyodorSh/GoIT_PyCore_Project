from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, value):

        if len(value) != 12:
            raise ValueError("Перевірте чи вірно ви ввели номер")

        if not value.isnumeric():
            raise ValueError("Вводу підлягають лише цифри")

        if not value.startswith(38):
            raise ValueError("Номер має бути такого вигляду: 380505555555 ")

        self._value = value


class Email(Field):
    @Field.value.setter
    def value(self, value):
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$", value):
            raise ValueError("Перевірте вірність вводу email")

        self._value = value




class Birthday(Field):
    pass


class Note(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.note = None


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
