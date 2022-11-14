import re
from collections import UserDict
from datetime import datetime


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


class Address(Field):
    @Field.value.setter
    def value(self, value):
        if len(value) == 0:
            raise ValueError("Настільки короткої адреси існувати не може")
        self._value = value


class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        today = datetime.now().date()
        birthday = datetime.strptime(value, "%Y-%m-%d").date()
        if birthday > today:
            raise ValueError("Помилкова дата дня народження")

        self._value = value


class Note:
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None

    def add_phone(self, phone):
        pass


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def get_record(self, name):
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]


address_book = AddressBook()
