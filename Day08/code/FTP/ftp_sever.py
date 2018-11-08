'''
ftp 文件服务器程序
fork server训练
'''

from socket import *
import os,sys
import time

class FtpServer():
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        print('Execute List')
        #获取文件列表
        file_list = os.listdir(FILE_PATH)

        if not file_list:
            self.connfd.send(b'This file storage is empty')
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        files = ''
        for file in file_list:

            if file[0] != '.' and os.path.isfile(FILE_PATH + file):
                files =files + file +'#'

        #将拼接好的文件名字符串发送给客户端        
        self.connfd.send(files.encode())
    
    def do_quit(self):
        self.connfd.close()
        sys.exit('Client quit')

    def do_download(self,filename):
        try:
            fd = open(FILE_PATH+filename , 'rb')
        except:
            self.connfd.send('This file does not exist'.encode())
            return
        else:
            self.connfd.send('OK'.encode())
            time.sleep(0.1)

        #发送文件内容
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        fd.close()
        print('Download is over')
            

    def do_upload(self,filename):
        try:
            fd = open(FILE_PATH+filename, 'wb')
        except:
            self.connfd.send('Upload failed'.encode())
            return
        else:
            self.connfd.send('OK'.encode())
            time.sleep(0.1)

        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
            fd.close()
            print('Upload is over')
        



            



            

#全局变量
HOST = '0.0.0.0'
PORT = 1234
ADDR = (HOST,PORT)
FILE_PATH = '/home/tarena/AID1808/PythonNet/Day08/code/FTP/file/'

#创建网络连接
def main():
    #创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(25)

    print('Listen the port 1234')

    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit('Close server')
        except Exception as e:
            print('Error:',e)
            continue
        print('Connect to client :',addr)

        #创建子进程
        pid = os.fork()
        
        if pid == 0:

            p = os.fork()

            if p == 0:  #接受客户端请求
                sockfd.close()

                #为没个子进程创建实例对象
                ftp = FtpServer(connfd)

                while True:

                    data = connfd.recv(1024).decode()

                    if not data or data[0] == 'Q':
                        ftp.do_quit()

                    elif data[0] == 'L':
                        ftp.do_list()

                    elif data[0] == 'D':
                        filename = data.split(' ')[-1]
                        ftp.do_download(filename)
                    elif data[0] == 'U':
                        filename = data.split(' ')[-1]
                        ftp.do_upload(filename)

            else:
                os._exit(0)
        else:
            connfd.close()
            os.wait()

if __name__ == '__main__':
    main()

