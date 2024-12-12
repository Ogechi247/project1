from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509 import CertificateSigningRequestBuilder
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.serialization import load_pem_private_key

def generate_csr(container_name):
    # Load the container's private key
    key_file = f"{container_name}_key.pem"
    with open(key_file, "rb") as f:
        private_key = load_pem_private_key(f.read(), password=None)

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

# Generate CSRs for all containers
# generate_csr("Jason Ossai")
# generate_csr("Oge Ofili")
# generate_csr("Adrienne M")
