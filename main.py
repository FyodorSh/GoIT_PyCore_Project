from parse_utils import get_handler


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
