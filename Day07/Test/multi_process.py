#多线程
from test import *
import multiprocessing
import time

def io():
    write()
    read()



jobs = []
t = time.time()
for i in range(10):
    p = multiprocessing.Process(target = io)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
print('Process CPU:',time.time()-t)