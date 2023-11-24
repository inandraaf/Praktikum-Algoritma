import modul

daftar = """
Pilihan yang tersedia
h = Menampilkan bantuan ini
a = Menampilkan NIM
b = Menampilkan Nama
c = Menampilkan Alamat
d = Menampilkan Kode Pos
e = Menampilkan Kelas
f = Menampilkan Fakultas
g = Menampilkan Hobi
i = Keluar
"""
print(daftar)

for i in range(1000) :
    user = input(str("Pilihan Anda = "))
    if user == 'h' :
        print(daftar)
    elif user == 'a':
        modul.tampilkanNIM()
    elif user == 'b':
        modul.tampilkanNama()
    elif user == 'c':
        modul.tampilkanAlamat()
    elif user == 'd':
        modul.tampilkanKodePos()
    elif user == 'e':
        modul.tampilkanKelas()
    elif user == 'f':
        modul.tampilkanFakultas()
    elif user == 'g':
        modul.tampilkanHobi()
    elif user == 'i':
        print("Terima kasih.")
        break
    else :
        print('Mohon maaf pilihan tidak ada')
        print(daftar)
