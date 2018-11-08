from multiprocessing import Pool
from time import sleep



def child(name):  
    sleep(2)
    print('name is',name)

pool =Pool()

for i in range(5):
    msg = i

    r = pool.apply_async(func = child, args = (msg,))


pool.close()
pool.join()
