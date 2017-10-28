import socketserver
import pickle


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.server.clients += 1
        self.type = self.request.recv(1024).decode()
        print('{} {}:{}:{}'.format(self.type, self.server.clients, self.client_address[0], self.client_address[1]))
        if self.type == 'Server':
            server.servers = self.client_address
        elif self.type == 'Client':
            self.request.sendall(pickle.dumps(server.servers))


if __name__ == '__main__':
    CONNECTION = ('0.0.0.0', 8080)
    server = socketserver.TCPServer(CONNECTION, TCPHandler)
    server.clients = 0
    server.servers = []
    server.serve_forever()
