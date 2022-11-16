import difflib
from operations import OPERATIONS


def parse_input(user_input):
    command = user_input
    data = ''
    for key in OPERATIONS:
        if user_input.strip().lower().startswith(key):
            command = key
            data = user_input[len(command):]
            break
    if data:
        return callback(command)(data.lstrip())
    try:
        return callback(command)()
    except KeyError:
        return find_command(command)


def callback(command):
    return OPERATIONS[command]


def find_command(wrong_command):
    similar_commands = difflib.get_close_matches(wrong_command, OPERATIONS.keys(), n=5, cutoff=0.4)
    if similar_commands:
        return f'{wrong_command} is not found, maybe you mean these: {", ".join(similar_commands)}'
    else:
        return 'Wrong command'


