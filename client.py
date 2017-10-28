import socket
import pickle

HOST, PORT = '192.168.0.5', 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    client.sendall('Client'.encode())
    HOST, PORT = pickle.loads(client.recv(1024))
    client.close()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.sendall('hello'.encode())

finally:
    client.close()
