from exceptions import CommandError, PathError
import parse_utils


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as e:
            print(f"Key Error - {e}")
        except ValueError as e:
            print(f"Value Error - {e}")
        # except CommandError:
        #     command_prefix = ' '.join(command for command in args[0][:args[1]])
        #     print(f"Wrong command - {command_prefix} {args[0][args[1]]}")
        #     correct_commands = parse_utils.find_command(args[0][args[1]])
        #     if correct_commands:
        #         print('Try:')
        #         for correct_command in correct_commands:
        #             print(f"  {command_prefix} {correct_command}")
    return wrapper


# def similar_command(func):
#     def wrapper(*args):
#         try:
#             return func(*args)
#         except KeyError as e:
