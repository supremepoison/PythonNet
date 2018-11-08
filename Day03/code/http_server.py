from socket import *

#创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',1238))
    sockfd.listen(10)
    print('Listen to the port 1238')
    while True:
        connfd, addr = sockfd.accept()
        #处理请求
        handleClient(connfd)
        connfd.close()


#接受request 发送response
def handleClient(connfd):
    request=connfd.recv(4096)
    #将request按行切割
    request_lines = request.splitlines()
    for line in request_lines:
        print(line)

    try:
        f = open('/home/tarena/AID1808/PythonNet/Day03/code/index.html')
    except IOError:
        response = "HTTP/1.1 404 Not Found \r\n"
        response += '\r\n' #空行
        response += "****Sorry*****"
    else:
        response = "HTTP/1.1 200 Ok \r\n"
        response += '\r\n' #空行
        response += f.read()
    finally:
        connfd.send(response.encode())
        

        
    #暂时不做解析
    # response = connfd.send()

if __name__ == '__main__':
    main()
    
