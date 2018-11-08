from socket import *
#添加HTTP响应
#创建TCP套接字
s = socket()
s.bind(('0.0.0.0',5555))
s.listen(10)

while True:
    c,addr = s.accept()
    print('Connect form',addr)
    data = c.recv(4096)
    print('***************************')
    print(data)
    print('***************************')
    data = '''HTTP/1.1 200 ok
    Content-Encoding:gzip
    Content-Type:text/html

    <head><meta charset = 'utf-8' /></head>
    <h1>Welcome to hell</h1>
    <p>你你你借款分类登记了</p>
    '''
    c.send(data.encode())   #发送给浏览器
    c.close()

s.close()