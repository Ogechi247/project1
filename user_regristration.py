import json
import getpass
import bcrypt

USERS_FILE = 'users.json'

def load_users():
    """Load user data from the JSON file."""
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    """Save user data to the JSON file."""
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def register_user():
    users = load_users()

    full_name = input("Enter Full Name: ")
    email = input("Enter Email Address: ")
    password = getpass.getpass("Enter Password: ")
    re_password = getpass.getpass("Re-enter Password: ")

    if password != re_password:
        print("Passwords do not match. Please try again.")
        return

    if email in users:
        print("User already registered.")
        return

    # Hash the password before saving
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    users[email] = {
        'full_name': full_name,
        'password': hashed_password  # Store the hashed password
    }

    save_users(users)
    print("User Registered.")
    print("Exiting SecureDrop.")
