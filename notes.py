FILE = "notes.txt"

def add_note():
    note = input("Enter note: ")
    with open(FILE, "a") as file:
        file.write(note + "\n")
    print("Note added.")

def view_notes():
    try:
        with open(FILE, "r") as file:
            notes = file.readlines()

        if not notes:
            print("No notes found.")
        else:
            print("\nNotes:\n")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")

    except FileNotFoundError:
        print("No notes file found.")

def search_notes():
    keyword = input("Enter keyword: ")
    try:
        with open(FILE, "r") as file:
            notes = file.readlines()

        print("\nSearch Results:\n")
        for note in notes:
            if keyword.lower() in note.lower():
                print(note.strip())

    except FileNotFoundError:
        print("No notes found.")

def delete_note():
    try:
        with open(FILE, "r") as file:
            notes = file.readlines()

        view_notes()
        index = int(input("\nEnter note number to delete: ")) - 1

        if 0 <= index < len(notes):
            notes.pop(index)

            with open(FILE, "w") as file:
                file.writelines(notes)

            print("Note deleted.")
        else:
            print("Invalid number.")

    except:
        print("Error deleting note.")

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        search_notes()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
