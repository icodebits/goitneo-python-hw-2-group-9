def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError as e:
            return "Give me the name please."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if contacts.get(name) != None:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f'{name} not found.'

@input_error
def show_phone(args, contacts):
    name = args[0]
    if contacts.get(name) != None:
        return contacts[name]
    else:
        return f'{name} not found.'

def show_all(contacts):
    all_contacts = []
    if contacts:
        for name, phone_number in contacts.items():
            all_contacts.append(f'{name}: {phone_number}')
        return '\r\n'.join(all_contacts)
    else:
        return 'The contact list is empty'

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()