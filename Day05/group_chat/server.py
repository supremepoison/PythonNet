#coding = ufg-8
'''
Chatroom
env:python 3.5
socket and fork
'''

from socket import * 
import os,sys

#创建网络连接
def main():
    ADDR = ('0.0.0.0',4567)

    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    
    pid = os.fork()
    if pid< 0:
        print('Failed')
        return
    elif pid == 0:
        while True:
            msg = input('Administrator:')
            msg = 'c Administrator '+ msg
            s.sendto(msg.encode(),ADDR)


    else:
        #用于接受各种客户端请求,调用相应的函数处理
        do_request(s)


def do_request(s):
    #存储结构 {'张桑':('127.0.0.0.1',9999)}
    user = {}
    while True:
        msg, addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')

        if msgList[0] == 'L':
            do_login(s,user,msgList[1],addr)

        if msgList[0] == 'c':
            msg = ' '.join(msgList[2:])
            do_chat(s,user,msgList[1],msg)

        if msgList[0] == 'Q':
            do_quit(s,user,msgList[1])
       
def do_login(s,user,name,addr):
    if (name in user) or name == 'Administrator':
        s.sendto('This user already exist'.encode(),addr)
        return
    s.sendto(b'Ok',addr)

    #通知其他人
    msg = '\nWelcome %s into chat room' % name
    for i in user:
        s.sendto(msg.encode(),user[i])

    #将用户加入字典
    user[name] = addr
    # print(user)

def do_chat(s,user,name,msg):
    msg = '\n%s say: %s'%(name,msg)
    for i in user:
        if i !=name:
            s.sendto(msg.encode(),user[i])

def do_quit(s,user,name):
    msg = '\n%s quit chat room' % name
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    #从字典删除用户
    del user[name]
        






if __name__ == '__main__':
    main()
