## Kegiatan 1. Perulangan. Oleh : Inandra Asha Fardhana

N = {'Segitiga' : 'L = 0.5 * a * t',
     'Persegi' : 'L = s ** 2',
     'Persegi panjang' : 'L = p * l',
     'Lingkaran' : 'L = pi * r ** 2',
     'Jajaran genjang' : 'L = a * t'}

print('''
No  | Nama Bangun      | Rumus Luas
----|------------------|----------------
1   | Segitiga         |  %s
2   | Persegi          |  %s      
3   | Persegi panjang  |  %s
4   | Lingkaran        |  %s
5   | Jajaran genjang  |  %s
'''%(N['Segitiga'], N['Persegi'], N['Persegi panjang'],
     N['Lingkaran'], N['Jajaran genjang']))
     
