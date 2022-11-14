from commands import exit_function, hello_function, add_record, del_record, change_phone, delete_phone, email_func, \
    birthday_func, next_birthday_func, address_func, show_function, search_function
from notes_commands import add_note, show_notes, add_tags, delete_note, edit_note, search_notes

OPERATIONS = {

    'stop': exit_function,
    'exit': exit_function,
    'close': exit_function,
    'good bye': exit_function,
    'hello': hello_function,
    'hi': hello_function,
    'add email': email_func,
    'add birthday': birthday_func,
    'add address': address_func,
    'add note': add_note,
    'add tags': add_tags,
    'search notes': search_notes,
    'add': add_record,
    'days to birthday': next_birthday_func,
    'change phone': change_phone,
    'show all': show_function,
    'search': search_function,
    'delete phone': delete_phone,
    'delete': del_record,
    'delete notes': delete_note,
    'edit notes': edit_note,
    'show notes': show_notes
}