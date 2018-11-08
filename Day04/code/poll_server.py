from socket import *
from select import *
#创建关键的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',5678))
s.listen(25)

#创建一个poll对象
p = poll()

#建立查找字典
fdmap = {s.fileno():s}

#注册要关注的IO
p.register(s, POLLIN | POLLERR)
while True:
    #监控IO
    print('阻塞等待IO')
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('Connect from:',addr)

            #添加新的关注事件
            p.register(c, POLLIN | POLLHUP)
            fdmap[c.fileno()] = c

        elif event & POLLIN: 
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print('Receive from client:',data.decode())
                fdmap[fd].send('Receive your msg'.encode())


