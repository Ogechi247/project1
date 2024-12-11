import sys
from getpass import getpass
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Function to encrypt the file
def encrypt_file(public_key_file, input_file):
    # Read the recipient's public key
    with open(public_key_file, 'rb') as f:
        public_key = RSA.import_key(f.read())

    # Generate a random symmetric key (AES)
    symmetric_key = get_random_bytes(32)  # AES-256 key

    # Encrypt the file with the symmetric key
    cipher_aes = AES.new(symmetric_key, AES.MODE_GCM)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)

    # Encrypt the symmetric key with the recipient's public key
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_key = cipher_rsa.encrypt(symmetric_key)

    # Write the encrypted data (overwriting the original file)
    with open(input_file, 'wb') as f:
        for x in (encrypted_key, cipher_aes.nonce, tag, ciphertext):
            f.write(x)

    print("Encryption Successful.")

# Function to decrypt the file
def decrypt_file(private_key_file, input_file):
    # Prompt the user for the passphrase to decrypt the private key
    passphrase = getpass("Enter the passphrase for your private key: ")

    # Read the recipient's private key
    with open(private_key_file, 'rb') as f:
        private_key = RSA.import_key(f.read(), passphrase=passphrase)

    # Read the encrypted file
    with open(input_file, 'rb') as f:
        encrypted_key = f.read(256)  # RSA encrypted symmetric key (256 bytes)
        nonce = f.read(16)  # AES nonce (16 bytes)
        tag = f.read(16)  # AES tag (16 bytes)
        ciphertext = f.read()  # The encrypted file content

    # Decrypt the symmetric key with the recipient's private key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    symmetric_key = cipher_rsa.decrypt(encrypted_key)

    # Decrypt the file with the symmetric key
    cipher_aes = AES.new(symmetric_key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)

    # Write the decrypted content to the output file
    with open(input_file, 'wb') as f:
        f.write(plaintext)

    print("Decryption Successful.")

# Main function to handle command-line arguments
def main():
    if len(sys.argv) != 4:
        print("Usage: python3 fcrypt.py --encrypt/--decrypt <key-file> <file>")
        sys.exit(1)

    operation = sys.argv[1]
    key_file = sys.argv[2]
    input_file = sys.argv[3]

    if operation == '--encrypt':
        encrypt_file(key_file, input_file)
    elif operation == '--decrypt':
        decrypt_file(key_file, input_file)
    else:
        print("Invalid operation. Use --encrypt or --decrypt.")
        sys.exit(1)

if __name__ == '__main__':
    main()
