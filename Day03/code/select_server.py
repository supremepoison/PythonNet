from socket import *
from select import select 

#创建套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',9876))
s.listen(25)

#添加到关注列表
rlist = [s]
wlist = []
xlist = []

while True:
    #IO监控
    rs, ws, xs = select(rlist,wlist,xlist)

    for r in rs:
        #如果r is s说明 s 就绪即有客户端发起连接
        if r is s:

            c,addr = r.accept()
            print('Connect from ',addr)
            rlist.append(c)

        #某个客户端连接套接字就绪,接受消息
        else:

            data = r.recv(1024)

            if not data:                
                rlist.remove(r)
                r.close()
                continue
            print('Receive:',data.decode())

            # r.send('Receive your msg'.encode())
            wlist.append(r)

    for w in ws:
        
        w.send('Receive your msg'.encode())
        wlist.remove(w)

    for x in xs:
        x.close()
        raise
