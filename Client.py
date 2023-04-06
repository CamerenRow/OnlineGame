import socket
import threading
port = 5555

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect(('192.168.1.196', port))
print('Connected!')
print(socket_client.recv(1024).decode())
while True:
    choice = (input("Choose 'heads(1)' or 'tails(2)': "))

    socket_client.sendall(choice.encode())

    result = socket_client.recv(1024).decode()

    print(result)


