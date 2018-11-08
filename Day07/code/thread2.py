from threading import Thread
from time import sleep

#线程函数

def fun(sec,name):
    print('线程参数传递')
    sleep(sec)
    print('%s线程执行完毕'% name)

#创建多个线程执行
thread = []
for i in range(3):
    t = Thread(target = fun, args = (2,), kwargs = {'name':'John%d'%i})
    thread.append(t)
    t.start()

for i in thread:
    i.join()