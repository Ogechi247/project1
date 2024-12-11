from Crypto.PublicKey import RSA

# Generate an RSA key pair (private and public keys)
key = RSA.generate(2048)

# Export the private key
private_key = key.export_key()
with open("private.pem", "wb") as private_file:
    private_file.write(private_key)

# Export the public key
public_key = key.publickey().export_key()
with open("public.pem", "wb") as public_file:
    public_file.write(public_key)

print("RSA key pair generated and saved as 'private.pem' and 'public.pem'.")
