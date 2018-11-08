from multiprocessing import Process,Array
import time
#创建共享内存,将列表放入共享内存
# shm = Array('i',[1,2,3,4,5])
#在共享内容开辟5个整型空间
# shm = Array('i',5)

#存入字符串
shm = Array('c',b'hello')


def fun():
    for i in shm:
        print(i)
    shm[0] = b's'


p = Process(target = fun)
p.start()
p.join()

for i in shm:
    print(i,end = ' ')
print()
print(shm.value.decode())