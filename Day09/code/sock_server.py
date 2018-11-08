from socketserver import *


#服务器类型
class Server(ForkingMixIn,TCPServer):
    pass
#处理具体请求
class Handler(StreamRequestHandler):
    #具体处理方法
    def handle(self):
        print('Connect form:',self.client_address)
        while True:
            #self.request == accept返回的客户端连接套接字
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'Receive')

if __name__ == '__main__':
    server_addr = ('0.0.0.0',1234)

    #创建服务器
    server = Server(server_addr, Handler)
    server.serve_forever()#启动服务器