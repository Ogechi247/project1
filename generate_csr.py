from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509 import CertificateSigningRequestBuilder
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from getpass import getpass

def generate_csr():
    # Ask for the container name
    container_name = input("Enter the container name: ")

    # Determine the private key file name
    key_file = "private.pem"  # Default private key file name for Adrienne

    # Ask for the password for the private key
    password = getpass("Enter the password for the private key: ").encode()

    try:
        # Load the container's private key
        with open(key_file, "rb") as f:
            private_key = load_pem_private_key(f.read(), password=password)

        # Create a CSR
        csr = (
            CertificateSigningRequestBuilder()
            .subject_name(
                x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, container_name)])
            )
            .sign(private_key, hashes.SHA256())
        )

        # Save the CSR to a file
        csr_file = f"{container_name}.csr.pem"
        with open(csr_file, "wb") as f:
            f.write(csr.public_bytes(serialization.Encoding.PEM))

        print(f"CSR for {container_name} created: {csr_file}")
    except FileNotFoundError:
        print(f"Error: Private key file '{key_file}' not found.")
    except ValueError as e:
        print(f"Error: Unable to load private key. {e}")

# Generate CSR
if __name__ == "__main__":
    generate_csr()
