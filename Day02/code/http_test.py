from socket import *

#创建TCP套接字
s = socket()
s.bind(('0.0.0.0',2500))
s.listen(10)

while True:
    c,addr = s.accept()
    print('Connect form',addr)
    data = c.recv(4096)
    print('***************************')
    print(data)
    print('***************************')
    c.close()

s.close()