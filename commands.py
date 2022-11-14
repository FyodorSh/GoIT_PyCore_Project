from classes import address_book, Record
from decorator import input_error


@input_error
def exit_function():
    """Function for saving and closing program"""
    address_book.save_to_file()
    return "good bye"


@input_error
def hello_function():
    """Function for starting bot and loading previous savings"""
    try:
        address_book.load_from_file()
    except:
        pass
    return 'How can i help you?'


@input_error
def add_record(data):
    name, *phones = data.split(' ')
    if name in address_book:
        raise ValueError('This contact already exist.')
    record = Record(name)

    for phone in phones:
        record.add_phone(phone)

    address_book.add_record(record)
    return f'You added new contact: {name} with this {phones}.'


@input_error
def change_phone(data):
    name, *phones = data.split(' ')
    record = address_book[name]
    record.change_phones(phones)
    return 'You changed phones.'


@input_error
def delete_phone(data):
    name, phone = data.split(' ')

    record = address_book[name]
    if record.delete_phone(phone):
        return f'Phone {phone} for {name} contact deleted.'
    return f'{name} contact does not have this number'


@input_error
def search_function(value):

    records = address_book.search(value)

    search_records = '\n'.join([record.get_info() for record in records])
    return search_records


@input_error
def show_function():
    contacts = ''
    page_number = 1

    for page in address_book.iterator():
        contacts += f'Page №{page_number}\n'

    for record in page:
        contacts += f'{record.get_info()}\n'
        page_number += 1

    return contacts


@input_error
def birthday_func(data):
    name, birthday_date = data.split(" ")
    record = address_book[name]
    record.add_birthday(birthday_date)
    return f"{birthday_date} Дата дня народження створена"


def next_birthday_func(name):
    name = name.strip()
    record = address_book[name]
    return f"Святкувати будем через {record.get_days_to_next_birthday()} днів"


@input_error
def address_func(data):
    name, address_date = data.split(" ")
    record = address_book[name]
    record.add_address(address_date)
    return f"{address_date} Тут проживає гарна людина"


@input_error
def email_func(data):
    name, email_date = data.split(" ")
    record = address_book[name]
    record.add_email(email_date)
    return f"{email_date} На цю пошту ми можемо щось надіслати)"


@input_error
def del_record(name):
    address_book.remove_record(name)
    return "You deleted the contact."
