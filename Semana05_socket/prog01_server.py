import socket
import sys

arquivo = sys.argv[1]
porta = int(sys.argv[2])


with open(arquivo, 'r') as file:
    arq = file.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), porta))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f'connection from {address} has been established!')
    clientsocket.send(bytes(arq, 'utf-8'))
    