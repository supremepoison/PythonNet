import os

filename = './test.txt'
#获取文件大小
size = os.path.getsize(filename)
print(size)
# f = open(filename,'rb')
#父子进程公用一个文件对象偏移量会相互影响


#child
def child():
    f = open(filename,'rb')
    n = size // 2
    fw = open('children.txt', 'wb')

    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()

def father():
    f= open(filename,'rb')
    fw = open('father.txt','wb')
    f.seek(size//2,0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

pid = os.fork()

if pid < 0: 
    print('Error')
elif pid == 0:
    child()
else:
    father()