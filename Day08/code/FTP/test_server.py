from socket import *
import time
import os,sys

class FtpServer():
    def __init__(self,connfd):
        self.connfd = connfd
    
    def do_list(self):
        print('Execute list')

        file_list = os.listdir(FILE_PATH)

        if not file_list:
            self.connfd.send(b'There is empty')
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)
        
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH+file):
                files = files + file +'#'

        self.connfd.send(files.encode())   

    def do_quit(self):
        self.connfd.close()
        sys.exit('Client quit')

    def do_download(self,filename):
        print('Execute download')
        try:
            f = open(FILE_PATH+filename, 'rb')
        except:
            self.connfd.send(b'Does not exist.')
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)    

        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        f.close()
        print('Download is over')
    
    def do_upload(self,filename):
        print('execute upload')
        try:
            f = open(FILE_PATH+filename, 'wb')
        except:
            self.connfd.send(b'upload file failed')
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)

        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(1024)
        f.close()
        print('Upload is over')

        
            
                




HOST = '0.0.0.0'
PORT = 1234
ADDR = (HOST,PORT)
FILE_PATH= '/home/tarena/AID1808/PythonNet/Day08/code/FTP/file/'
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(25)

    print('Listen the port%d'%PORT)
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit('close server')
        except Exception as e:
            print(e)
            continue
        print('Connect to client :',addr)

        pid = os.fork()
        if pid==0:
            p =os.fork()
            if p ==0:
                sockfd.close()
                ftp = FtpServer(connfd)
                while True:
                    data = connfd.recv(1024).decode()

                    if not data  or data[0] == 'Q':
                        ftp.do_quit()
                    elif data[0] == 'L':
                        ftp.do_list()
                    elif data[0] == 'D':
                        filename = data.split(' ')[-1]
                        ftp.do_download(filename)
                    elif data[0] =='U':
                        filename = data.split(' ')[-1]
                        ftp.do_upload(filename)

            else:
                os._exit(0)

        else:
            connfd.close()
            os.wait()




if __name__ == '__main__':
    main()