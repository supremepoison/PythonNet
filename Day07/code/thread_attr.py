from threading import Thread,currentThread
from time import sleep
def fun():
    sleep(3)
    print('线程属性测试')
    #获取当前线程对象
    print('执行%s线程对象'%currentThread().getName())


t  = Thread(target = fun, name = 'Tarena')

#p判断主线程退出对子线程的影响
t.setDaemon(True)
t.daemon = True

t.start()

print('Thread name:',t.name)

t.setName('Ball')
print('Thread get name:',t.getName())

#线程状态
print('is alive',t.is_alive())

# t.join()
print('*********主线程结束************')