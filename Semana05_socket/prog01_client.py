import socket
import sys

ip = sys.argv[1]
porta = int(sys.argv[2])
arquivo = sys.argv[3]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), porta))

msg = s.recv(1024)
file = open(arquivo, 'w')
file.write(msg.decode('utf-8'))
