from classes import address_book, Record
from sort_files import run_sorting


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


def del_record(name):
    address_book.remove_record(name)
    return "You deleted the contact."


def folder_sorting(path_to_folder):
    return run_sorting(path_to_folder)
