from Crypto.PublicKey import RSA
from getpass import getpass

# Load the encrypted private key
with open("private.pem", "rb") as private_file:
    encrypted_private_key = private_file.read()

# Prompt the user for the passphrase to decrypt the private key
passphrase = getpass("Enter your passphrase to unlock the private key: ")

try:
    private_key = RSA.import_key(encrypted_private_key, passphrase=passphrase)
    print("Private key successfully loaded.")
except ValueError as e:
    print("Failed to load private key. Please check your passphrase.")
