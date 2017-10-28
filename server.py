import socket
import socketserver


class Client:
    def getInstance(self):
        self.host, self.port = self.client.getsockname()
        print(self.host, self.port)
        self.client.close()
        return self.host, self.port

    def __init__(self):
        HOST, PORT = '192.168.0.5', 8080
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client.connect((HOST, PORT))
        self.client.sendall('Server'.encode())


class Server(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request.recv(1024).decode())


if __name__ == '__main__':
    # CONNECTION = Client().getInstance()
    CONNECTION = Client().getInstance()
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer(CONNECTION, Server)
    server.serve_forever()
