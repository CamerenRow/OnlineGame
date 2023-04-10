import socket
import threading
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.196', port))
print('Connected!')


isGaming = False


def Recieve():
    while True:
        try:
            data = s.recv(1024).decode()
            print(data)
        except:
            # server is probably closed
            s.close()
t = threading.Thread(target=Recieve)
t.start()


while True:
    user_input = input()
    s.sendall(user_input.encode('utf-8'))