from socketserver import *

class Server(ThreadingMixIn,UDPServer):
    pass

class Handler(DatagramRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline()
            if not data:
                break
            print(data.decode())
            self.wfile.write(b'Receive')

if __name__ == "__main__":
    server = Server(('0.0.0.0',1234),Handler)
    server.serve_forever()
