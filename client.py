# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65433  # The port used by the server
print("Number of packets to send: ")
NumberOfPackets=int(input())
print("Size of packets to send: ")
SizeOfPackets=int(input())
packets=[SizeOfPackets] * NumberOfPackets

print(packets)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(data)
    data = s.recv(1024)

print(f"Received {data!r}")