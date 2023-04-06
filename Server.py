import socket
import threading
import random
port = 5555

players = {}
choices = {}
player_id = 1

Clients = []


def Handle_Client(client_socket, client_address, player_id, players, choices):
    while True:
        if client_socket.recv(1024).decode():

            if client_socket.recv(1024).decode().isdigit():
                choice = int(client_socket.recv(1024).decode())

                print(choice)
                if choice not in [1, 2]:
                    client_socket.sendall(
                        'Invalid choice, please choose heads(1) or tails(2)'.encode())
                continue
            choices[player_id] = choice
            if len(choices) == 2:
                print('here')
                player1_choice = choices[1]
                player2_choice = choices[2]

                result = random.randint(1, 2)
                print(f'the result is {result}')

                if(player1_choice == player2_choice):
                    guessed_result = "It's a tie"
                elif player1_choice == result:
                    guessed_result = "player 1 wins"
                else:
                    guessed_result = "player 2 wins"

                players[1].sendall(guessed_result.encode())
                players[2].sendall(guessed_result.encode())

                # reset choices dictionary
                choices.clear()


def Chat_Room(client_socket, client_address):
    print(f'Connected to {client_address}')
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                Clients.remove(client_socket)
                print(f"Client disconnected: {client_address}")
                break
        except:
            print(f'Client {client_address} disconected')
            Clients.remove(client_socket)
            client_socket.close()
            break

        print(msg)
        if msg.startswith('/CF'):
            t = threading.Thread(target=Handle_Client, args=(
                client_socket, client_address, player_id, players, choices))
            t.start()

        for client in Clients:
            if client != client_socket:
                client.sendall(msg.encode())
                


socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(('192.168.1.196', port))

socket_server.listen(2)
print('looking for connections')


while True:
    client_socket, client_address = socket_server.accept()
    Clients.append(client_socket)
    print(f'Connection established with {client_address}')

    players[player_id] = client_socket

    t = threading.Thread(target=Chat_Room, args=(
        client_socket, client_address))
    t.start()
    player_id += 1
