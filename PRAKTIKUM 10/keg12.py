import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50001))
while pesan.lower() != "Keluar" :
    pesan = raw_input("Perintah : ")
    s.send(pesan)
    if pesan.lower() == "Keluar":
        s.close()
        break
    elif pesan.lower() != "Keluar" :
        response = s.recv(1024)
        print "Jawab : ", response
s.close()
        
