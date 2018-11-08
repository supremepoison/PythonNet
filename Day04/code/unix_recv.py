from socket import *

#确定套接字文件
sock_file = '/home/tarena/AID1808/PythonNet/Day04/code/sock'

#创建本地套接字
s = socket(AF_UNIX,SOCK_STREAM)

#绑定套接字文件
s.bind(sock_file)

#监听
s.listen(25)

while True:
    c,addr = s.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("Receive:",data.decode())
    c.close()
s.close()