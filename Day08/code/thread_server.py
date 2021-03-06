from socket import *
from threading import *
import sys

HOST = '0.0.0.0'
PORT = 1234
ADDR = (HOST,PORT)


#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(25)

#客户端处理函数
def handler(c):
    print('Connect from',c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive')
    c.close()


#接受客户端请求
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit('Server Close')
    except Exception as e:
        print(e)
        continue

    t = Thread(target = handler,args= (c,))
    t.setDaemon(True)
    t.start()
    

