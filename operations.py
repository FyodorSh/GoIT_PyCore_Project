from commands import exit_function, hello_function, add_record, del_record, change_phone, delete_phone

OPERATIONS = {

    'stop': exit_function,
    'exit': exit_function,
    'close': exit_function,
    'good bye': exit_function,
    'hello': hello_function,
    'hi': hello_function,
    'add': add_record,
    'change phone': change_phone,
    'delete phone': delete_phone,
    'delete': del_record
}