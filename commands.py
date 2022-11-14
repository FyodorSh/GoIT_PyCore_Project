from classes import address_book, Record


def exit_function():
    """Function for close program"""
    return "good bye"


def hello_function():
    return 'How can i help you?'


def add_record(data):
    name, *phones = data.split(' ')
    if name in address_book:
        raise ValueError('This contact already exist.')
    record = Record(name)

    for phone in phones:
        record.add_phone(phone)

    address_book.add_record(record)
    return f'You added new contact: {name} with this {phones}.'


def change_phone(data):
    name, *phones = data.split(' ')
    record = address_book[name]
    record.change_phones(phones)
    return 'You changed phones.'


def delete_phone(data):
    name, phone = data.split(' ')

    record = address_book[name]
    if record.delete_phone(phone):
        return f'Phone {phone} for {name} contact deleted.'
    return f'{name} contact does not have this number'


def del_record(name):
    address_book.remove_record(name)
    return "You deleted the contact."
