import classes
import decorator
from exceptions import CommandError
from operations import OPERATIONS


def find_command(wrong_command):
    commands = {}
    max_overlap = 0
    for command in OPERATIONS:
        count = 0
        word_len = len(wrong_command) if len(wrong_command) < len(command) else len(command)
        for i in range(word_len):
            if wrong_command[i] == command[i]:
                count += 1
            if wrong_command[::-1][i] == command[::-1][i]:
                count += 1
        commands[command] = count
        max_overlap = count if count > max_overlap else max_overlap

    return [k for k, v in commands.items() if v == max_overlap]


def get_handler(command_list):
    return read_command_list(command_list)


@decorator.input_error
def get_func(command_list: list, iter: int, command_name: str):
    try:
        command = OPERATIONS[command_name]
    except KeyError:
        raise CommandError
    iter += 1
    if command == read_command_list:
        command = read_command_list(command_list, iter)
    else:
        for _ in range(iter):
            command_list.pop(0)
    return command


def read_command_list(command_list: list, iter=0):
    command_name = command_list[iter].lower()
    return get_func(command_list, iter, command_name)


test_rec = classes.AddressBook()
