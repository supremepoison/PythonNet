'''

ftp 文件服务器程序
fork client训练

'''

from socket import *
import sys
import time
#将具体功能实现放在类中
class FtpClient():
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')
        #等待回复
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for i in files:
                print(i)
            print('Show file list above')


        else:
            #无法执行操作
            print(data)
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit('See you ')

    def do_download(self,filename):

        self.sockfd.send(('D '+filename).encode())
        data = self.sockfd.recv(1024).decode()

        if data == 'OK':
            fd = open(filename,'wb')

            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)

            fd.close()
            print('%s Download successfully'%filename)
        
        else:
            print(data)

    def do_upload(self,filename):
        try:
            f = open(filename,'rb')
        except:
            print('There is no file')
            return

        self.sockfd.send(('U '+filename).encode())
        data = self.sockfd.recv(1024).decode()

        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
            print('%s Upload successfully'%filename)
        else:
            print(data)
        




#网络连接
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print('Connect to server failed:',e)
        return

    ftp = FtpClient(sockfd)

    while True:
        print('--------Options---------')
        print('***                  ***')
        print('***      List        ***')
        print('***  Download File   ***')
        print('***  Upload File     ***')
        print('***      Quit        ***')
        print('***------------------***')
        print()

        cmd = input('Command>>')

        if cmd.strip() == 'list':
            ftp.do_list()

        elif cmd.strip() == 'quit':
            ftp.do_quit()

        elif cmd[:3] == 'dow':
            filename = cmd.split(' ')[-1]
            ftp.do_download(filename)
        elif cmd[:2] == 'up':
            filename = cmd.split(' ')[-1]
            ftp.do_upload(filename)

        else:
            print('Enter the right command')

if __name__ == '__main__':
    main()
        


