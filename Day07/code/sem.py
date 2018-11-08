from multiprocessing import Semaphore,Process
from time import sleep
import os

#创建信号量

sem = Semaphore(3)

def fun():
    print('%d 想执行事件' % os.getpid())
    #消耗一个信号量,有信号量则不阻塞
    sem.acquire()
    print('%d执行想执行的事件'% os.getpid())
    sleep(3)
    print('%d事件执行完毕' % os.getpid())

jobs = []

for i in range(5):
    p = Process(target = fun)
    jobs.append(p)
    p.start()

for i in range(3):
    sleep(5)
    sem.release() #增加一个信号量

for i in jobs:
    i.join()

print(sem.get_value())