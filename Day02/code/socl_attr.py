from socket import * 

s = socket()
#设置端口可以立即使用
#测试式,防止总是换端口
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))


#套接字类型
print(s.type)

#套接字地址族
print(s.family)

#获取套接字绑定地址
s.bind(('127.0.0.1',1111))
print(s.getsockname())

#文件描述符
print(s.fileno())

s.listen(3)

c,addr = s.accept()
#客户端连接套接字获取对应客户端地址
print(c.getpeername())