from socket import *

#创建套接字

sockfd = socket()

#发起连接

server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

#发收消息

    
data = input('>>')

sockfd.send(data.encode())

n = sockfd.recv(1024)
print('From server:',n.decode())

sockfd.close()
