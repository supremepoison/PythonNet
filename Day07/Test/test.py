#计算密集型函数

def count(x,y):
    c = 0
    while c < 7000000:
        c +=1
        x +=1
        y +=1
#单进程: Line cpu: 7.773900747299194
#多线程: Thread CPU: 8.020527601242065
#多进程: Process CPU: 4.740935325622559

#IO密集型
def write():
    f = open('test','w')
    for i in range(1200000):
        f.write('hello world \n')
    f.close()

def read():
    f = open('test')
    lines =f.readline()
    f.close()
#单进程 Line IO: 5.183574199676514
#多线程: Thread IO: 2.26147723197937
#多进程: Process IO: 1.2537996768951416