from socket import *

#创建套接字

sockfd = socket()

#发起连接

server_addr = ('127.0.0.1',4888)
sockfd.connect(server_addr)

#发收消息

data = open('hello.txt', 'rb')

while True:
    r = data.read(1024)
    sockfd.send(r)
    if not r:
        break

    n = sockfd.recv(1024)
print('From server:',n.decode())

data.close()

sockfd.close()
