import socket

#创建套接字

sockfd = socket.socket(socket.AF_INET,
                    socket.SOCK_STREAM)

#设置绑定地址

sockfd.bind(('0.0.0.0', 4888))

#设置监听

sockfd.listen(5)

#接受客户端连接
print('Waiting for connect...')

    #等待处理客户端连接
connfd,addr = sockfd.accept()
print('Connect from ',addr ) #打印客户端地址

#收发消息
f = open('test.txt','wb')

while True:
    data = connfd.recv(1024)

    f.write(data)
    if not data:
        break


    # else:
    print('Message:', data) 
    connfd.send('Receive'.encode())     
    
f.close()

#关闭套接字
connfd.close()

sockfd.close()   
    

