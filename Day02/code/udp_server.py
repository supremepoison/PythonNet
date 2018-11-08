from socket import *


#创建数据报套接字

sockfd =socket(AF_INET,SOCK_DGRAM)


#绑定地址

server_addr = ('0.0.0.0', 8888)
sockfd.bind(server_addr)

#消息接受/发送
while True:

    data, addr = sockfd.recvfrom(1024)
    print('Receive message from %s:%s'%(addr, data.decode()))
    sockfd.sendto(b'Thanks for your msg',addr)

sockfd.close()

