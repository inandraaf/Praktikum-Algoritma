import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50007))
s.listen(5)
print "server siap"
perintah = ""
a = 0
t = 0
while perintah != "keluar":
    komm, addr = s.accept()
    while perintah != "keluar":
        item = komm.recv(1024).lower().split("=")
        perintah = item[0]
        if perintah == "keluar":
            komm.send("done")
            s.close()
            break
        print "pesan : ", perintah
        if len(item) == 2:
            if perintah == "alas":
                a = int(item[1])
                komm.send("alas disimpan")
            elif perintah == "tinggi":
                t = int(item[1])
                komm.send("tinggi disimpan")
            else:
                komm.send("perintah tidak diketahui")
        elif perintah == "hitung":
            L = float((4*(0.5*a*t))+ (a*a))
            response = "Luas piramid dengan alas {} dan tinggi {} adalah {}".format(a, t, L)
            komm.send(response)
        else:
            komm.send("pesan tidak diketahui")
