import json

contacts_FILE = 'contacts.json'

def load_users():
    """Load user data from the JSON file."""
    try:
        with open(contacts_FILE, 'r') as file:
            userinfo = json.load(file)
            return userinfo
    except FileNotFoundError:
        return {}

def save_users(users):
    """Save user contacts to the JSON file."""
    with open(contacts_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def main():
    users = load_users()
    print("Welcome to SecureDrop.")

    while True:
        answer = input("Type help For Commands: ").strip().lower()

        if answer == 'help':
            print("add -> Add a new contact \nlist -> List all online contacts \nsend -> Transfer file to contact \nexit -> Exit SecureDrop")

        elif answer == 'add':
            full_name = input("Enter Full Name: ")
            email = input("Enter Email Address: ")
            # Add the new contact to the users dictionary
            users[full_name] = {'email': email}
            # Save the updated users to the file
            save_users(users)
            print(f"Contact {full_name} added successfully.")

        elif answer == 'list':
            if users:
                print("Contacts:")
                for name, info in users.items():
                    print(f"{name}: {info['email']}")
            else:
                print("No contacts found.")

        elif answer == 'exit':
            print("Exiting SecureDrop.")
            break  # Exit the loop and end the program

        else:
            print("Unknown command. Type 'help' for the list of commands.")

# Run the main function
main()
