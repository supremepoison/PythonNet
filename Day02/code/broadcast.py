from socket import *

#创建套接字
s = socket(AF_INET,SOCK_DGRAM)
#设置发送可以接受广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.bind(('0.0.0.0',3222))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print('from{} get broadcast:{}'.format(addr,msg.decode()))
    except KeyboardInterrupt:
        print('quit accept')
        break
    except Exception as e:
        print(e)
        
s.close()