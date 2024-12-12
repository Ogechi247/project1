import socket

def udp_broadcast():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    message = input("Enter a message to broadcast: ").encode()
    client.sendto(message, ("<broadcast>", 9999))
    print("Broadcast sent.")


# Send a UDP broadcast
udp_broadcast()
