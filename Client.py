import socket
import threading
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.196', port))
print('Connected!')

def CoinFlip():
   while True:
      print('heads(1) or tails(2)')
      choice = int(input())
   
def Recieve():
   while True:
      data = s.recv(1024).decode()
      print(data)
    
t= threading.Thread(target=Recieve)
t.start()

while True:
   msg = input()

   if msg.startswith('/CoinFlip'):
        t= threading.Thread(target=CoinFlip)
        t.start()
        break
   else:
      s.sendall(msg.encode())


