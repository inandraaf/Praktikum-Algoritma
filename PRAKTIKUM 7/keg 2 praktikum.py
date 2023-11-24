## Kegiatan 2. Password. Oleh : Inandra Asha Fardhana

x = 1
for i in range(3) :
    password = input("Masukkan password : ")
    x += 1
    if password == "Nandra" :
        print("Anda berhasil login.")
        break
    elif x > 3 :
        print("Anda telah mencoba 3 kali. Akses anda ditolak.")
    else :
        print("Maaf, anda salah memasukan password")
        
            
                         
