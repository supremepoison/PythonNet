import os  
from time import sleep

def length():
    data = open('test.txt','br')
    r =data.read()
    l =len(r)
    data.close()

    if l / 2 == 0:
        a = int(l/2)        
    else:
        a = int((l+1)/2 )   
    return a

def child():
    r_msg = open('test.txt','br')
    a = r_msg.read(length())

    w_msg = open('children.txt','bw')
    w_msg.write(a)

    r_msg.close()
    w_msg.close()

def father():
    r_msg = open('test.txt','br')
    r_msg.seek(length())
    b = r_msg.read(length())

    w_msg = open('father.txt','bw')
    w_msg.write(b)

    r_msg.close()
    w_msg.close()

pid = os.fork()

if pid < 0:

    print('Failed')
elif pid == 0:
    child()   
else:
    father()
    
