from exceptions import CommandError, PathError
import parse_utils


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as exeption:
            return (f"Key Error - {exeption}, Ви ввели невірне ім'я")
        except ValueError as exeption:
            return exeption.args[0]
        except TypeError:
            return ("Помилкова команда")
        except IndexError:
            return ("Вводити потрібно (Ім'я та наступна інформація)")
        except PathError:
            return ("Потрібно ввести корректний шлях до папки.")
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
