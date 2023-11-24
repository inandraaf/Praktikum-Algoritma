#Client TCP untuk server p_tcpser.py

import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50003))
while pesan.lower() != 'q':
    pesan = input('Kirim : ')
    s.send(pesan)
    if pesan.lower() != 'q' :
        response = s.recv(1024)
        print('Diterima: ', response)
s.close()
