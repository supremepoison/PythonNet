from multiprocessing import Process
from time import sleep,ctime


def tm():
    for i in range(4):
        sleep(2)
        print(ctime())


p = Process(target = tm, name = 'evil')

p.daemon = True  #需要在start前运行

p.start()
print('Process name', p.name)
print('Process PID', p.pid)
print('Process alive', p.is_alive())


p.join()