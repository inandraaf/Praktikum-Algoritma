## Kegiatan 3. Ucapan selamat. Oleh : Inandra Asha Fardhana

w = ('pagi', 'siang', 'sore', 'petang', 'malam')
nama = input("Masukkan nama saudara : ")
waktu = float(input("Pukul berapa sekarang? "))

if waktu >= 4.00 and waktu <= 10.00 :
    print("Selamat", w[0], nama)
elif waktu >= 10.00 and waktu <= 14.00 :
    print("Selamat", w[1], nama)
elif waktu >= 14.00 and waktu <= 18.30 :
    print("Selamat", w[2], nama)
elif waktu >= 18.30 and waktu <= 21.00 :
    print("Selamat", w[3], nama)
else :
    print("Selamat", w[4], nama)



              
