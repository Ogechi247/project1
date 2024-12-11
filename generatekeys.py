from Crypto.PublicKey import RSA
from getpass import getpass

# Generate an RSA key pair (private and public keys)
key = RSA.generate(2048)

# Ask the user for a passphrase to encrypt the private key
passphrase = getpass("Enter a passphrase to protect your private key: ")

# Export the private key encrypted with the passphrase
private_key = key.export_key(passphrase=passphrase, pkcs=8, protection="scryptAndAES128-CBC")
with open("private.pem", "wb") as private_file:
    private_file.write(private_key)

# Export the public key (public keys are typically not encrypted)
public_key = key.publickey().export_key()
with open("public.pem", "wb") as public_file:
    public_file.write(public_key)

print("RSA key pair generated.")
print("Private key is protected with your passphrase and saved as 'private.pem'.")
print("Public key saved as 'public.pem'.")
