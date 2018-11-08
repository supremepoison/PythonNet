from select import select
from socket import *

s = socket()
s.bind(('0.0.0.0',4567))
s.listen(25)

#关注套接字事件IO
print('监控IO')
rs, ws, xs = select([s],[],[],3)
print('处理IO')

