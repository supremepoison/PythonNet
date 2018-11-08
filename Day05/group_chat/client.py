#coding = ufg-8
'''
Chatroom
env:python 3.5
socket and fork
'''

from socket import * 
import os,sys

#创建套接字
def main():
    #从命令行输入服务器地址
    if len(sys.argv)<3:
        print('argc is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)

    while True:
        name = input('Enter your name:')
        msg = 'L ' + name
        #发送给服务端
        s.sendto(msg.encode(), ADDR)
        #等待回应
        data,addr = s.recvfrom(1024)
        if data.decode() == 'Ok':
            print('Welcome')
            break
        else:
            print(data.decode())

    #创建父子进程
    pid = os.fork()
    if pid < 0:
        sys.exit('Create process failed')
    elif pid == 0:
        send_msg(s,name,ADDR)
    else:
        recv_msg(s)
#发送消息
def send_msg(s,name,ADDR):
    while True:
        text = input('BB:')

        if text == 'quit':
            msg = 'Q '+ name
            s.sendto(msg.encode(),ADDR)
            sys.exit('Quit chat room')

        msg = 'c %s %s' % (name,text)
        s.sendto(msg.encode(),ADDR)
    

#接受消息
def recv_msg(s):
    while True:
        data, addr = s.recvfrom(2048)
        #接收服务发来的退出
        # 标志后退出该进程
        if data.decode() == 'EXIT':
            sys.exit(0)
        print(data.decode()+'\nBB:', end = '')












        
if __name__ == '__main__':
    main()
