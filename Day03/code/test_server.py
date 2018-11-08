from select import select
from  socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',3456))
s.listen(25)

rlist = [s]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            rlist.append(c)
        else:
            data = c.recv(1024)
            if not data:
                rlist.remove(c)
                r.close()
                continue
            print(data.decode())
            wlist.append(r)
    for w in ws: 
        w.send('hello'.encode())
        wlist.remove(w)

