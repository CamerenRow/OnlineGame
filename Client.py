import socket
import threading
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.196', port))
print('Connected!')


def CoinFlip():
    while True:
        print('heads(1) or tails(2)')
        choice = str(input())
        s.sendall(choice.encode())

        result = s.recv(1024).decode('utf8')
        print(result)


def Recieve():
    while True:
        try:
            data = s.recv(1024).decode()
            print(data)
            if data.startswith('/CF'):
                s.send(data.encode())
                t = threading.Thread(target=CoinFlip)
                t.start()
            break
        except:
            # server is probably closed
            s.close()

def send_message():
    while True:
      msg = input()
      s.sendall(msg.encode())
      break

t = threading.Thread(target=Recieve)
t.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()
