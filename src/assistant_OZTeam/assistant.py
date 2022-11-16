from src.assistant_OZTeam.classes import address_book
from src.assistant_OZTeam.notes import user_notes
from src.assistant_OZTeam.parse_utils import parse_input


def main():
    try:
        while True:
            command_input = input("Enter command: ")
            result = parse_input(command_input)
            print(result)
            if result == 'good bye':
                break
    finally:
        address_book.save_contacts_to_file()
        user_notes.save_notes_to_file()


if __name__ == "__main__":
    main()
