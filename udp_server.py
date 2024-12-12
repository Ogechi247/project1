import socket

def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("0.0.0.0", 9999))

    print("Listening for broadcasts...")
    while True:
        data, addr = server.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")

# Run the UDP server
udp_server()
