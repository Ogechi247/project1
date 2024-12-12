from getpass import getpass
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
import datetime
import random

def create_ca():
    try:
        # Generate CA private key
        ca_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

        # Prompt for a passphrase
        passphrase = getpass("Enter a passphrase to protect the CA private key: ").encode()

        # Save the CA private key protected by the passphrase
        with open("ca_key.pem", "wb") as f:
            f.write(ca_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.BestAvailableEncryption(passphrase)
            ))

        # Generate and sign the CA certificate
        ca_cert = (
            x509.CertificateBuilder()
            .subject_name(x509.Name([
                x509.NameAttribute(NameOID.COMMON_NAME, "Centralized CA")
            ]))
            .issuer_name(x509.Name([
                x509.NameAttribute(NameOID.COMMON_NAME, "Centralized CA")
            ]))
            .public_key(ca_key.public_key())
            .serial_number(random.randint(1, 2**32))
            .not_valid_before(datetime.datetime.utcnow())
            .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=3650))
            .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
            .add_extension(x509.SubjectKeyIdentifier.from_public_key(ca_key.public_key()), critical=False)
            .sign(ca_key, hashes.SHA256())
        )

        # Save the CA certificate
        with open("ca_cert.pem", "wb") as f:
            f.write(ca_cert.public_bytes(serialization.Encoding.PEM))

        print("CA private key and certificate generated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_ca()
