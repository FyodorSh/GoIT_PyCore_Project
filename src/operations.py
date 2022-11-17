from commands import (exit_function, hello_function, add_record, del_record, change_phone, delete_phone, email_func,
                      birthday_func, next_birthday_func, address_func, show_function, search_function, folder_sorting,
                      search_birthday_func, add_phone_func, get_help)
from notes_commands import add_note, show_notes, add_tags, delete_note, edit_note, search_notes, search_notes_by_tags,\
    sort_notes


OPERATIONS = {
    'help': get_help,
    'stop': exit_function,
    'exit': exit_function,
    'close': exit_function,
    'good bye': exit_function,
    'hello': hello_function,
    'hi': hello_function,
    'add email': email_func,
    'add phone': add_phone_func,
    'add birthday': birthday_func,
    'add address': address_func,
    'add note': add_note,
    'add tags': add_tags,
    'search notes': search_notes,
    'search tags': search_notes_by_tags,
    'sort notes': sort_notes,
    'search by tags': search_notes_by_tags,
    'add record': add_record,
    'days to birthday': next_birthday_func,
    'birthdays in range': search_birthday_func,
    'change phone': change_phone,
    'show all': show_function,
    'search': search_function,
    'delete phone': delete_phone,
    'delete record': del_record,
    'delete notes': delete_note,
    'edit notes': edit_note,
    'show notes': show_notes,
    'sort folder': folder_sorting
}
