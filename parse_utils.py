import classes
import decorator
from exceptions import CommandError
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
    return callback(command)()


def callback(command):
    return OPERATIONS.get(command, break_func)


def break_func():
    # commands_variants = f"Wrong command - {command}"
    # correct_commands = find_command(command)
    # if correct_commands:
    #     commands_variants += '\n Try: \n '
    #     for correct_command in correct_commands:
    #         commands_variants += f"{correct_command}"
    # return commands_variants
    return 'Wrong command'

# def find_command(wrong_command):
#     commands = {}
#     max_overlap = 0
#     for command in OPERATIONS:
#         count = 0
#         word_len = len(wrong_command) if len(wrong_command) < len(command) else len(command)
#         for i in range(word_len):
#             if wrong_command[i] == command[i]:
#                 count += 1
#             if wrong_command[::-1][i] == command[::-1][i]:
#                 count += 1
#         commands[command] = count
#         max_overlap = count if count > max_overlap else max_overlap
#
#     return [k for k, v in commands.items() if v == max_overlap]

