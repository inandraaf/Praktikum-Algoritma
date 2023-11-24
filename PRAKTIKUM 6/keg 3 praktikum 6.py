Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\HP\OneDrive\Documents\KULIAH\PRAKTIKUM ALGORITMA PEMROGRAMAN\keg 2 praktikum 6.py
Inandra Asha Fardhana
14 Oktober 2003
I.A.Fardhana
I142003
Ina140

= RESTART: C:\Users\HP\OneDrive\Documents\KULIAH\PRAKTIKUM ALGORITMA PEMROGRAMAN\keg 2 praktikum 6.py
Inandra Asha Fardhana
14 Oktober 2003
I.A.Fardhana
I142003
Ina898
Nama = "Inandra Asha Fardhana"
NIM = "L200220045"
X = "1" + NIM[7:]
a = int(X)
b = len(Nama)

type(a)
<class 'int'>
# karena nilai dalam variabel a telah diubah ke integer
type(b)
<class 'int'>
>>> # karena terdapat instruksi len yang akan menghasilkan jumlah dari karakter yang ber tipe data integer
>>> a / b
49.76190476190476
>>> # karena hasil dari 1045 dibagi 21 adalah 49.76190476190476
>>> a // b
49
>>> # karena pembulatan dari pembagian 1045 dan 21 adalah 49
>>> 10 * (a-999)
460
>>> # karena hasil dari 1045 dikurangi 999 dikali 10 adalah 460
>>> b ** 2
441
>>> # karena hasil kuadrat dari 21 adalah 441
>>> a % b
16
>>> # karena sisa dari pembagian 1045 dan 21 adalah 16
>>> 
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #karena data dalam variabel c merupakan bentuk pecahan
>>> a / c
83.6
>>> # karena hasil pembagian 1045 dan 12.5 adalah 83.6
>>> a // c
83.0
>>> # karena pembulatan dari pembagian 1045 dan 12.5 adalah 83.0
>>> a % c
7.5
>>> # karena sisa dari pembagian 1045 dan 12.5 adalah 7.5
>>> 
>>> c > b
False
>>> # karena nilai c adalah 12.5 dan b adalah 21. Maka pernyataan c > b adalah salah
>>> type( c > b)
<class 'bool'>
>>> # karena c > b adalah pernyataan, sehingga hasil outputnya adalah antara True dan False
>>> a > b and b > c
True
>>> #karena nilai a = 1045 dan nilai b = 21, maka pernyataan a > b adalah benar. Karena nilai b = 21 dan nilai c = 12.5, maka pernyataan b > c adalah benar. Sehingga pernyataan a > b and b > c adalah True
>>> a > 1100 or b < 10
False
>>> # karena pernyataan 1045 > 1100 salah. Pernyataan 21 < 10 adalah salah. Sehingga a > 1100 or b < 10 adalah False (False or False = False)
>>> 
