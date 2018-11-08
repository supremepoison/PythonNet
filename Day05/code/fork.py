import os
from time import sleep

print('***********')
a = 1
pid = os.fork()

if pid < 0:
    print('Create process failed')
elif pid == 0:
    print('Child process')
    print('a = %d'%a)
    a = 1000
else:
    sleep(1)
    print('Parent proces')
    print('p',a)
print('all',a)