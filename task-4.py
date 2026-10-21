"""A simple console assistant for managing contacts."""


def parse_input(user_input):
    """Split user input into a lowercase command and its arguments."""
    # Split the input string into parts based on whitespace
    parts = user_input.split()
    # If the input is empty, return an empty command and no arguments
    if not parts:
        return ("",)

    # Unpack the first part as the command and the rest as arguments
    command, *args = parts
    # Return the command in lowercase along with its arguments
    return command.lower(), *args


def add_contact(args, contacts):
    """Add or replace a contact and return a status message."""
    # Check if the correct number of arguments is provided (2: name and phone)
    if len(args) != 2:
        return "Usage: add username phone"

    # Unpack the arguments into name and phone
    name, phone = args
    # Add or replace the contact in the contacts dictionary
    contacts[name] = phone
    # Return a message indicating the contact was added
    return "Contact added."


def change_contact(args, contacts):
    """Change an existing contact's phone number."""
    if len(args) != 2:
        return "Usage: change username phone"

    # Unpack the arguments into name and phone
    name, phone = args
    # Check if the contact exists in the contacts dictionary
    if name not in contacts:
        return "Contact not found."

    # Update the contact's phone number
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    """Return the phone number for a contact."""
    if len(args) != 1:
        return "Usage: phone username"

    # Unpack the argument into name
    name = args[0]
    # Check if the contact exists in the contacts dictionary
    if name not in contacts:
        return "Contact not found."

    # Return the contact's phone number
    return contacts[name]


def show_all(contacts):
    """Return all saved contacts as a formatted string."""
    # Check if there are any contacts saved
    if not contacts:
        return "No contacts saved."

    # Return all contacts as a formatted string
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    """Run the assistant command loop."""
    # Initialize an empty dictionary to store contacts
    contacts = {}
    # Print a welcome message to the user
    print("Welcome to the assistant bot!")

    # Start an infinite loop to continuously prompt the user for commands
    while True:
        try:
            # Prompt the user for input and store it in the variable user_input
            user_input = input("Enter a command: ")
        # Handle exceptions for end-of-file (EOF) or keyboard interrupt (Ctrl+C)
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            break

        # Parse the user input into a command and its arguments
        command, *args = parse_input(user_input)

        # Check if the command is "close" or "exit" to terminate the loop
        if command in ("close", "exit"):
            print("Good bye!")
            break
        # Handle the "hello" command by greeting the user
        if command == "hello":
            print("How can I help you?")
        # Handle the "add" command to add a new contact
        elif command == "add":
            print(add_contact(args, contacts))
        # Handle the "change" command to update an existing contact's phone number
        elif command == "change":
            print(change_contact(args, contacts))
        # Handle the "phone" command to display a contact's phone number
        elif command == "phone":
            print(show_phone(args, contacts))
        # Handle the "all" command to display all contacts
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

# If the script is being run directly (not imported as a module), call the main function.
if __name__ == "__main__":
    main()
