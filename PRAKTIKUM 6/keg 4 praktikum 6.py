Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Inandra Asha Fardhana"
>>> NIM = 145
>>> Tinggi = 1.67
>>> Berat = 85
>>> TahunLahir = 2003
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # karena variabel aku berisi kumpulan data dari beberapa variabel. Dan ditandai dengan tanda kurung biasa
>>> Aku[0]
2003
>>> # karena karakter indeks ke-0 dari variabel Aku adalah Tanggallahir, yaitu 2003
... a = NIM % 4; Aku[a]
85
>>> # karena hasil bagi dari 145 dibagi 4 adalah 1. Lalu menampilkan karakter indeks ke-1 dari variabel A adalah Berat = 85
>>> type(Aku[a])
<class 'int'>
>>> # karena indeks ke-1 adalah berat yang bernilai 85. Itu merupakan tipe data integer
>>> Aku[a:4]
(85, 1.67, 145)
>>> # karena instruksi menampilkan indeks ke 1 sampai ke 3. Yang ditampilkan adalah Berat, Tinggi, dan NIM
>>> type(Aku[a:4])
<class 'tuple'>
>>> # karena berisi beberapa kumpulan variabel yang berisi data
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # karena tuple tidak bisa diubah elemennya
>>> type(Data)
<class 'list'>
>>> # karena variabel Data berisi kumpulan data yang ditandai dengan tanda kurung siku
>>> type(Data[4])
<class 'str'>
>>> # karena karakter indeks ke-4 pada list adalah Nama yang bertipe data string
>>> Data[4][5]
'r'
>>> # karena instruksi memanggil indeks ke-4 pada list, yaitu Nama. Selanjutnya memanggil indeks ke-5 pada nama yaitu huruf "r"
>>> Data[4][a:6]
'nandr'
>>> # karena instruksi memanggil indeks ke-4 pada list, dan yang ditampilkan adalah indeks ke 1 sampai dengan 5
>>> Data [0] = 'ok' ; Data
['ok', 85, 1.67, 145, 'Inandra Asha Fardhana']
# pada list, elemen datanya bisa diubah
>>> Data[-a]
'Inandra Asha Fardhana'
# karena instruksi indeks negatif adalah memanggil data terakhir. Pada list data terakhir adalah Nama
>>> range(a)
range(0, 1)
# karena kita ingin menambilkan range dari 0 sampai nilai a
