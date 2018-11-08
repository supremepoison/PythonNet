#coding=utf-8
'''
HTTP Server v2.0
多线程并发
可以做request解析
能够返回简单的数据
使用类进行封装
'''

from socket import *
from threading import Thread
import sys
import time

#封装具体的HTTPServer功能
class HTTPServer():
    def __init__(self,server_addr,static_dir):
        #添加对象属性
        self.server_addr=server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]

        #创建套接字
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_addr)



    def serve_forever(self):
       
        self.sockfd.listen(5)
        print('Listen the port %d' % self.port)
        while True:
            try:
                connfd, addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('服务器退出')
            except Exception as e :
                print('Error:',e)
                continue

            #创建线程处理客户端请求
            clientThread = Thread(target =self.handle, args = (connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    #具体处理客户端请求:
    def handle(self,connfd):
        #接受客户端请求
        request = connfd.recv(4096)
        #按行切割
        requestHeaders = request.splitlines()
        print(connfd.getpeername(),':',requestHeaders[0]) 

        #获取具体请求内容
        getRequest = str(requestHeaders[0]).split(' ')[1]
        print(getRequest)
        if getRequest == '/' or getRequest[-5:] =='.html':
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd,getRequest)
        connfd.close()

    #给客户端发送网页
    def get_html(self,connfd,getRequest):
        if getRequest == '/':
            filename = self.static_dir+'/index.html'
        else:
            filename = self.static_dir + getRequest
        
        try:
            f = open(filename)
        except Exception:
            #没找到网页
            response = "HTTP/1.1 404 Not Found \r\n"
            response += '\r\n' #空行
            response += "****Sorry*****"
        else:
            response = "HTTP/1.1 200 Ok \r\n"
            response += '\r\n' #空行
            response += f.read()
        finally:
            connfd.send(response.encode())
            f.close()

    def get_data(self,connfd,getRequest):
        urls = ['/time','/tedu','/python']
        if getRequest in urls:

            responseHeaders = 'HTTP/1.1 200 Ok\r\n'
            responseHeaders += '\r\n'

            if getRequest == '/time':
                responseBody = time.ctime()
            elif getRequest == '/tedu':
                responseBody = 'Get out of here!'
            elif getRequest == '/python':
                responseBody = 'This is a trick!'

        else:
            responseHeaders = 'HTTP/1.1 404 Not Found\r\n'
            responseHeaders += '\r\n'

            responseBody ='Are you kidding me ?'
        
        response = responseHeaders+responseBody
        connfd.send(response.encode())





        
                





if __name__ == '__main__':
    
    #用户使用时,自己设定服务器IP
    server_addr = ('0.0.0.0',1234)

    #需要用户提供网页位置
    static_dir = '/home/tarena/AID1808/PythonNet/Day09/static_html'

    #创建服务器对象
    httpd = HTTPServer(server_addr,static_dir)
   
 

    #启动服务器
    httpd.serve_forever()