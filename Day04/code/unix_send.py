from socket import *

s = socket(AF_UNIX,SOCK_STREAM)
sock_file = '/home/tarena/AID1808/PythonNet/Day04/code/sock'

s.connect(sock_file)

while True:
    a = input(">>")
    if not a:
        break
    s.send(a.encode())
s.close()