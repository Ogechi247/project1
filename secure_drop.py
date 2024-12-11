from user_registration import register_user

def main():
    print("No users are registered with this client.")
    register = input("Do you want to register a new user (y/n)? ").lower()

    if register == 'y':
        register_user()

if __name__ == "__main__":
    main()
