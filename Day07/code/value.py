from multiprocessing import Process,Value
import time
import random

#创建共享内存
money = Value('i',10000)

#操作共享内存增加

def man():
    for i in range(30):
        time.sleep(0.2)
        #符Value属性操作即对共享内存操作
        money.value +=random.randint(1,1000)


def girl():
    for i in range(30):
        time.sleep(0.16)
        money.value -= random.randint(100,900)

m = Process(target = man)
g = Process(target = girl)

m.start()
g.start()
m.join()
g.join()

print('一个月余额:',money.value)
