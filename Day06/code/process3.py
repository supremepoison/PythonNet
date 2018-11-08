from multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print('I am %s'%name)
        print('I am working ...')


# p = Process(target = worker, args = (2,'Spiderman'))
# p = Process(target = worker, kwargs = {'sec':2,'name' :'Spiderman'})
p = Process(target = worker, args = (2,), kwargs = {'name':'Spiderman'})


p.start()
p.join(4)
print('***********************')