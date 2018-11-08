import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Create process failed')
elif pid == 0:
    sleep(3)
    print('Child %d process exit' %os.getpid())
    os._exit(2)
else:
    #非阻塞等待
    while True:
        p,status = os.waitpid(-1,os.WNOHANG)
        print('Child pid:',p)
        print('child exit status:',os.WEXITSTATUS(status))
        sleep(1)
        if p != 0:
            break
    while True:
        print('Parent process...')
        sleep(2)
    