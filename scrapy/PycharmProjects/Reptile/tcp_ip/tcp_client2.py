import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 9998))

print(s.recv(1024).decode('utf-8'))
for data in [b'a2', b'b2', b'c2']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()