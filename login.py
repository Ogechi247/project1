import json
import os
import getpass
import bcrypt

Json_file = "users.json"

def load_users():
    """Load user data from the JSON file."""
    if os.path.exists(Json_file):
        with open(Json_file, 'r') as fd:
            return json.load(fd)
    return {}

def login():
    """Handle user login process."""
    userinfo = load_users()

    if not userinfo:
        print("No users are registered with this client. Please register first.")
        return

    emailaddress = input("Returning user, please enter your email address to login: ")
    if emailaddress in userinfo:
        password = getpass.getpass("Please enter your password: ")  # Input as plain text

        # Retrieve the stored hashed password
        hashed_password = userinfo[emailaddress]['password']

        # Check the provided password against the stored hash
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            print("Login successful! Welcome back.")
        else:
            print("Login failed. Please check your email or password and try again.")
    else:
        print("Email address not found. Please register first.")

if __name__ == "__main__":
    login()
