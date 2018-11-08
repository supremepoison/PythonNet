#创建二级子进程避免僵尸

import os
from time import sleep

def f1():
    sleep(3)
    print('事件1')

def f2():
    sleep(4)
    print('事件2')
    
pid = os.fork()

if pid < 0:
    print('Error')

elif pid == 0:

    p = os.fork()   #创建二级子进程

    if p == 0:  #二级子进程
        f2()

    else:
        os._exit(0)#一级子进程退出


else:
    os.wait()   #等待一级子进程
    f1()
