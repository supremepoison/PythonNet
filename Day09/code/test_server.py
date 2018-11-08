from socket import *
from threading import Thread
import sys
import time

class HTTPServer():
    def __init__(self,server_addr,static_dir):
        self.server_addr = server_addr
        self.static_dir = static_dir
        self.host = server_addr[0]
        self.port = server_addr[1]

        self.creat_socket()
    def creat_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_addr)

    def start_server(self):

        self.sockfd.listen(25)
        print('Listen the port %d'%self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('server quit')
            except Exception as e:
                print(e)
                continue

            clientthread = Thread(target = self.handle,args  = (connfd,))
            clientthread.setDaemon(True)
            clientthread.start()

    def handle(self,connfd):

        request = connfd.recv(4096)
        requestHeaders = request.splitlines()
        print(connfd.getpeername(),':',requestHeaders[0])

        getrequest = str(requestHeaders[0]).split(' ')[1]
        print(getrequest)

        if getrequest == '/' or getrequest[-5:] =='.html':
            self.get_html(connfd,getrequest)
        else:
            self.get_data(connfd,getrequest)
        connfd.close()

    def get_html(self,connfd,getrequest):
        if getrequest == '/':
            filename = self.static_dir+'/index.html'
        else:
            filename = self.static_dir+ getrequest

        try:
            f = open(filename)
        except Exception:
            response = 'HTTP/1.1 404 NOT Found \r\n'
            response +='\r\n'
            response +='***sorry'
        else:
            response = 'HTTP/1.1 200 Ok \r\n'
            response += '\r\n'
            response += f.read()
            f.close()
        finally:
            connfd.send(response.encode())
    
    def get_data(self,connfd,getrequest):
        urls = ['/time','/tedu','/python']
        if getrequest in urls:

            reponseHeaders = 'HTTP/1.1 200 ok \r\n'
            reponseHeaders += '\r\n'

            if getrequest == '/time':
                responseBody = time.ctime()
            elif getrequest == '/tedu':
                responseBody = 'Get out of here!'
            elif getrequest == '/python':
                responseBody = 'This is a trick!'

        else:
            reponseHeaders = 'HTTP/1.1 404 Not Found \r\n'
            reponseHeaders += '\r\n'

            responseBody = 'r u kidding me?'

        response = reponseHeaders+responseBody
        connfd.send(response.encode())
  
            
            


    



if __name__ == "__main__":

    server_addr = ('0.0.0.0',1234)

    static_dir = '/home/tarena/AID1808/PythonNet/Day09/static_html'

    httpd = HTTPServer(server_addr,static_dir)
    httpd.start_server()

