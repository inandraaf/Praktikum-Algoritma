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
    "keluar"    :   "Siap!!"
    }
while True :
    komm, addr = s.accept()
    while data.lower()!= "keluar" :
        data = komm.recv(1024)
        if data.lower() == "keluar":
            s.close()
            break
        print ("Perintah :",data)
        if kamus.has_key(data):
            komm.send(kamus[data])
        else :
            komm.send("Maaf, perintah tidak dimengerti.")
