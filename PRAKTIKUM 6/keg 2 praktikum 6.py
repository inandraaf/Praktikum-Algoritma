## Program Akun
## Dibuat oleh Inandra L200220045

import random
angka = random.randint(0,1000)

Nama = "Inandra Asha Fardhana"
Tanggallahir = "14 Oktober 2003"
NamaSingkat = Nama[0] + "." + Nama[8] + "." + Nama[13:21]
Username = Nama[0] + Tanggallahir[0:2] + Tanggallahir [11:16]
Password = Nama[0:3]+str(angka)

print(Nama)
print(Tanggallahir)
print(NamaSingkat)
print(Username)
print(Password)
