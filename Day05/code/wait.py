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
    pid,status = os.wait()
    print('Child pid:',pid)
    # 退出状态 * 256
    # print('child exit status:',status)
    print('child exit status:',os.WEXITSTATUS(status))

    print('Parent process...')
    while True:
        pass