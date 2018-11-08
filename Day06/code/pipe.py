from multiprocessing import Process,Pipe
import os,time
#如果单向管道,fd1-->recv
#           fd2-->send
fd1, fd2 = Pipe(False)
# fd1, fd2 = Pipe()


def fun(name):
    time.sleep(3)
    #向管道写入内容
    fd2.send(name)

jobs =[]
for i in range(5):
    p = Process(target = fun, args = (i,))
    jobs.append(p)
    p.start()

for i in range(5):
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()