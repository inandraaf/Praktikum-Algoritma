import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50001))
s.listen(5)
print("Program Komunikasi Tentang Data Diri")
data = ""
kamus = {
    "Nama"      :   "Inandra Asha Fardhana",
    "NIM"       :   "L200220045",
    "Angkatan"  :   "2022",
    "Keluar"    :   "Siap!!"
    }
while data.lower() != "Keluar":
    komm, addr = s.accept()
    while data.lower()!= "Keluar" :
        data = komm.recv(1024)
        if data.lower() == "Keluar":
            s.close()
            break
        print "Perintah :",data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else :
            komm.send("Maaf, perintah tidak dimengerti.")
