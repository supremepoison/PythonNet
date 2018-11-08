from socket import *
import os,sys

#创建套接字

ADDR = ('0.0.0.0',1234)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(25)

def client_handler(c):
    print('客户端:',c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive your msg')
    c.close()
    sys.exit(0) #将子进程销毁

#循环等待客户端连接
print('Listen to the port 1234 ')
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit('退出服务器')
    except Exception as e:
        print('Error:',e)
        continue
    #创建新的进程处理客户端请求

    pid = os.fork()

    #子进程处理客户端请求
    if pid == 0:

        p = os.fork()

        if p == 0:
            s.close()
            client_handler(c)    #客户端处理函数
        else:
            os._exit(0)

        
    #父进程或创建进程失败都继续等待下个客户端连接
    else:
        c.close()
        os.wait()
        continue

#客户端处理函数
