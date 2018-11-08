from socket import *
from time import sleep

dest = ('127.0.0.255',3222)

s = socket(AF_INET,SOCK_DGRAM)
#设置发送可以接受广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)



while True:
    sleep(2)
    s.sendto('Naruto'.encode(),dest)

s.close()

