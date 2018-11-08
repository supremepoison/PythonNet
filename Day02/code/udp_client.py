from socket import * 
import sys

if len(sys.argv) < 3:
    print('''
    argv is error!
    run as
    python3 udp_client.py 127.0.0.1 8888
    ''')
    raise


#从命令行接受服务器地址
HOST = sys.argv[1]
PORT = sys.argv[2]
ADDR = (HOST, int(PORT))

#创建数据报套接字

sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('Msg>>')
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print('Receive from server:',msg.decode())
sockfd.close()