import classes
import notes


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


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as e:
            print(f"Key Error - {e}")
        except ValueError as e:
            print(f"Value Error - {e}")
        except classes.CommandError:
            command_prefix = ' '.join(command for command in args[0][:args[1]])
            print(f"Wrong command - {command_prefix} {args[0][args[1]]}")
            correct_commands = find_command(args[0][args[1]])
            if correct_commands:
                print('Try:')
                for correct_command in correct_commands:
                    print(f"  {command_prefix} {correct_command}")
    return wrapper


def stop():
    quit()


def get_handler(command_list):
    return read_command_list(command_list)


@input_error
def get_func(command_list: list, iter: int, command_name: str):
    try:
        command = OPERATIONS[command_name]
    except:
        raise classes.CommandError
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
my_notes = notes.Notes()

OPERATIONS = {
    'good': read_command_list,
    'stop': stop,
    'add': read_command_list,
    'show': read_command_list,
    'note': my_notes.add_note,
    'notes': my_notes.show_notes
}


def main():
    while True:
        command = input("Enter command: ")
        command_list = command.strip().split(sep=" ")
        handler = get_handler(command_list)
        if handler is not None:
            if not command_list:
                handler()
            else:
                handler(command_list)


if __name__ == "__main__":
    main()
