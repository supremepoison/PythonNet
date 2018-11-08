import gevent
from gevent import monkey

monkey.patch_all()      #执行脚本插件,修改阻塞行为

from socket import *

#创建套接字

def server():
    s = socket()
    s.bind(('0.0.0.0',2345))
    s.listen(25)
    while True:
        c,addr = s.accept()
        print('Connect from', addr)
        #handle(c) #循环方案

        gevent.spawn(handle,c) #协程方案

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Recveive message')
    c.close()

server()