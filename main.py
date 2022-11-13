from parse_utils import parse_input


def main():
    while True:
        command_input = input("Enter command: ")
        result = parse_input(command_input)
        print(result)
        if result == 'good bye':
            break


if __name__ == "__main__":
    main()
