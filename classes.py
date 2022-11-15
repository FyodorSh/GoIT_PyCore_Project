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

        if not value.isnumeric():
            raise ValueError("Вводу підлягають лише цифри")

        if not value.startswith('38'):
            raise ValueError("На разі підтримуються тільки номера України (Приклад: 380995678344)")

        if len(value) != 12:
            raise ValueError("Перевірте довжину номера")

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
        if not value:
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
        self.address = None

    def get_info(self):

        birthday_info = ''
        email_info = ''
        address_info = ''

        phones_info = ', '.join([phone.value for phone in self.phones])

        if self.birthday:
            birthday_info = f' Birthday : {self.birthday.value}'

        if self.email:
            email_info = f' Email : {self.email.value}'

        if self.address:
            address_info = f' Address : {self.address.value}'

        return f'{self.name.value} : {phones_info[:-2]}{birthday_info}{email_info}{address_info}'

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False

    def change_phones(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)

    def add_birthday(self, birthday_data):
        self.birthday = Birthday(birthday_data)

    def get_days_to_next_birthday(self):
        if not self.birthday:
            raise ValueError("В цього контакту відсутня дата народження")

        today = datetime.now().date()
        birthday = datetime.strptime(self.birthday.value, "%Y-%m-%d").date()
        next_birthday_year = today.year

        if today.month >= birthday.month and today.day > birthday.day:
            next_birthday_year = next_birthday_year + 1

        next_birthday = datetime(
            year=next_birthday_year,
            month=birthday.month,
            day=birthday.day
        )

        return (next_birthday.date() - today).days

    def add_address(self, address_data):
        self.address = Address(address_data)

    def add_email(self, email_data):
        self.email = Email(email_data)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_record(self, name):
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def get_all_record(self):
        return self.data

    def search(self, value):
        record_result = []
        for record in self.get_all_record().values():
            if value in record.name.value:
                record_result.append(record)
                continue
            if record.email and value in record.email.value:
                record_result.append(record)
                continue
            for phone in record.phones:
                if value in phone.value:
                    record_result.append(record)
                    break

        if not record_result:
            raise ValueError("Контакту з таким значенням не існує.")
        return record_result

    def iterator(self, count=5):
        page = []
        i = 0

        for record in self.data.values():
            page.append(record)
            i += 1

            if i == count:
                yield page
                page = []
                i = 0

        if page:
            yield page

    def get_birthdays_in_range(self, value):
        birthdays = []
        if not value.isnumeric:
            raise ValueError("Потрібно ввести число")
        days = int(value)

        for record in self.data.values():
            if record.birthday and days >= record.get_days_to_next_birthday():
                birthdays.append(record)
        return birthdays


address_book = AddressBook()
