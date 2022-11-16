# GoIT_PyCore_Project

GoIT_PyCore_Project
\*\*

# Personal assistant bot

This project represents the implementation of a personal assistant with a command line interface. The project is installed as a Python package and can be called anywhere in the system by the appropriate command after installation;
This simple python app will help you to manage your contacts, notes and sort files on your computer.
Bot is compatible both with Windows and MacOS.
Tested on python 3, probably not compatible with python 2.

**Installation**
Download package, unpack it and use next command to install it from unpacked folder:

    pip install -e .

**Calling**
Launch comand line and use command `assistant`

## Description

A personal assistant can:

1.  Save contacts with names, addresses, phone numbers, emailі and birthdays to the contact book;
2.  Display a list of contacts who will have birthdays during a specified number of days from the current date;
3.  Can show how many days until a contact's next birthday.
4.  Check the correctness of the entered phone number and email when creating or editing a record and notify the user in case of incorrect input;
5.  Search for contacts from the contact book;
6.  Edit and delete data from the contact book;
7.  Keep notes with text information;
8.  Search for notes;
9.  Edit and delete notes;
10. Add "tags" to notes, keywords describing the topic and subject of the record;
11. Search and sort notes by keywords (tags);
12. Sort files in the specified folder by categories (images, documents, videos, etc.).
13. Also, when an incorrect command is entered, the bot analyzes the input and selects similar commands, displaying them to the user in the form of a prompt.

## How to use

### Address Book

You can use this bot to create your contacts book, in wich you can store Names, Phones, Emails, Birthdays and Addresses.
Below you can find information on all comands that you can use with examples. Commands are not case sensative.

#### Commands:

- [ ] **_hello_** or **_hi_** With this command yu can start working with bot

- [ ] **_add record ..._** With this command, the bot saves a new contact in memory. Instead of **...** the user enters the name and phone number(s), necessarily with a space.
      (_example:_ add record Dumbledore 380991231234 380671231234)

_Note_: _At this moment bot works only with ukrainian phones, it should starts with "38" and contain 12 digits._

- [ ] **_add phone ..._** With this command, the bot adds phone number to existing contact. Instead of **...** the user enters the name and phone number(s), necessarily with a space.
      (_example:_ add phone Dumbledore 380931231234)

- [ ] **_add email ..._** With this command, the bot adds email to existing contact. Instead of **...** the user enters the name and email, necessarily with a space.
      (_example:_ add email Dumbledore Albus.Dumbledore@hogwarts.uk)

- [ ] **_change phone ..._** With this command, the bot deletes old phones and stores the new phone number of the existing contact in memory. Instead of **...** the user enters the name, phone number needed to be changed and new phone number, necessarily with a space.
      (_example:_ change phone Dumbledore 380991231234 380441231234)

- [ ] - [ ] **_delete phone ..._** With this command, the bot deletes phone number to existing contact. Instead of **...** the user enters the name and phone number, necessarily with a space.
        (_example:_ add phone Dumbledore 380931231234)

- [ ] **_add address ..._** With this command, the bot adds address to existing contact. Instead of **...** the user enters the name and address, necessarily with a space.
      (_example:_ add address Dumbledore Headmaster's Office, Hogwarts Castle, Highlands, Scotland, Great Britain)

- [ ] **_show all_** With this command bot shows all contacts in your Address book.

- [ ] **_search ..._** With this command bot make search in the contact book, so that all information about one or more contacts can be found by entering instead of **…** a few digits of the phone number or letters of the name, email etc. And shows all contacts that has match.

- [ ] **_add birthday ..._** With this command, the bot adds birthday to existing contact. Instead of **...** the user enters the name and birthday in format: yyyy-mm-dd, necessarily with a space.
      (_example:_ add birthday Dumbledore 1881-08-24)

- [ ] **_days to birthday ..._** With this command, the bot shows the number of days until the contact's next birthday if the birthday is given. Instead of **...** the user enters the name of contact.
      (_example:_ days to birthday Dumbledore)

- [ ] **_birthdays in range ..._** With this command, the bot shows all contacts that will have birthdays during specified period of time starting from today.. Instead of **...** the user enters the period in days.
      (_example:_ birthdays in range 7)

- [ ] **_delete record ..._** With this command, the bot deletes contact from memory with all information related to it without possibility to restore it. Instead of **...** the user enters the name of contact, necessarily with a space.
      (_example:_ delete record Voldemort)

- [ ] **_stop, exit, close, good bye_** You can use any of these commands to exit application. All changes will be saved automaticaly.

## Files sorting

The function goes through the folder specified during the call of function and checks the file extension and, depending on the extension, make a decision to which category to assign this file and will move it to appropriate folder:

**"Audio":** [".mp3", ".aac", ".ac3", ".wav", ".amr", ".ogg"],
"**Video"**: [".mp4", ".mov", ".avi", ".mkv"],
**"Images"**: [".jpg", ".jpeg", ".png", ".svg", ".gif"],
**"Documents"**: [".doc", ".docx", ".txt", ".pdf", ".xls", ".xlsx", ".pptx", ".rtf"],
**"Books"**: [".fb2", ".epub", ".mobi"],
**"Archives"**: [".zip", ".rar", ".tar", ".gz"]

All other files remain unchanged.

Assistant will change name of file according to below rules:

- [ ] Transliterates the Cyrillic alphabet into Latin.

- [ ] Replaces all characters except Latin letters and numbers with
      underscore sign ('\_').
- [ ] Uppercase letters remain uppercase and lowercase remain lowercase after transliteration.

The archives will be unpacked and their contents will be transferred to "Archives" folder in subfolders named same as the archives.

All empty folders after sorting will be deleted.

#### Commands:

- [ ] **_sort folder ..._** With this command assistant sorts files in specified folder. Instead of **...** the user enters path to folder that needs sorting.
      (_example for Windows:_ sort folder C:\Users\HarryPotter\JunkFromRon)

## Notes

You can use this bot to create your personal text Notes with tags and manage it.
Below you can find information on all comands that you can use with examples. Commands are not case sensative.

- [ ] **_add note_** _<note text\>_ — With this command, the bot adds a new note. (_example_: add note It does not do well to dwell on dreams and forget to live.)
- [ ] **_show notes_** — With this command, the bot displays all notes with their "id" and tags.
- [ ] **_add tags_** <id\> <tag1 tag2 tag3...\> — a command for adding tags to a note. Tags are added to the note and stored as a list. Tags in a command are separated by spaces. You can add as many tags as you want.
      (_example_: add tags 1 quote Dumbledore book)
- [ ] **_edit notes_** <id/> <new note text/> – a command for editing a note. The text entered in the command replaces the previous data.
      (_example_: edit notes 3 To the well-organized mind, death is but the next great adventure.)
- [ ] **_delete notes_** <id\>– command to delete a note.
      (_example_: delete notes 13)

- [ ] **_search notes_** <text to search\>— a command for searching for a note by text. It will shows you all notes that will have matches with entered text.
      (_example_: search notes dreams)

- [ ] **_search tags_** <tag1 tag2 tag3...\>— a command for searching notes by tags.
      (_example_: search tags book quote)

- [ ] **_sort notes_** — With this command, the bot displays all notes in alphabetical order.
