import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50001))
while pesan.lower() != "q" :
    pesan = input("Send : ")
    s.send(bytes(pesan, 'utf-8'))
    if pesan.lower() == "q":
        s.close()
        break
    elif pesan.lower() != "q" :
        response = str(s.recv(1024))[2:-1]
        print ("Accepted : ", response)
s.close()
        
