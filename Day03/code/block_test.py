from socket import *
from time import sleep,ctime
#创建TCP套接字
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',6789))
sockfd.listen(25)

#设置非阻塞状态,一般和循环一起使用
sockfd.setblocking(False)

#设置超时时间
# sockfd.settimeout(5)
while True:
    print('Waiting for connect...')
    try:
        connfd,addr = sockfd.accept()
    #捕获非阻塞异常
    except BlockingIOError:
        sleep(1)

    #捕获超时异常
    # except timeout:
    #     print(ctime())
    #     continue
    else:
        print('Connect from',addr)
        data = connfd.recv(4096)
        print('Receive:',data.decode())
        connfd.close()
sockfd.close()
