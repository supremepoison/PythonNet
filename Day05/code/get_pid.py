import os
from time import sleep
import sys



pid = os.fork()

if pid< 0:
    print('Error')
elif pid == 0:
    sleep(1)
    print('CHild PID', os.getpid())
    print('Get parent PID',os.getppid())
    
else:
    print('Parent PID', os.getpid())
    print('Get child PID',pid)