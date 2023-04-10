import socket
import threading
import random
port = 5555

Clients = []




def Chat_Room(client_socket, client_address):
    print(f'Connected to {client_address}')
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                Clients.remove(client_socket)
                print(f"Client disconnected: {client_address}")
                break
        except:
            print(f'Client {client_address} disconected')
            Clients.remove(client_socket)
            client_socket.close()
            break

        for client in Clients:
            if client != client_socket:
                client.sendall(msg)


socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(('192.168.1.196', port))

socket_server.listen(2)
print('looking for connections')


while True:
    client_socket, client_address = socket_server.accept()
    Clients.append(client_socket)
    print(f'Connection established with {client_address}')

    t = threading.Thread(target=Chat_Room, args=(
        client_socket, client_address))
    t.start()
