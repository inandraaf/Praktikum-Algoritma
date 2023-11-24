def ubahF() :
    Celcius = float(input("Masukkan Suhu : "))
    UbahFah = float((9* Celcius) / 5 + 32)
    print("Suhu", Celcius, "Celcius setara dengan", UbahFah, "Fahrenheit")

def ubahC() :
    Fahrenheit = float(input("Masukkan Suhu : "))
    UbahCel = float((Fahrenheit - 32) * 5 / 9)
    print("Suhu", Fahrenheit, "Fahrenheit setara dengan", UbahCel, "Celcius")

def memilih() :
    print("Pilihlah fungsi konversi suhu yang disediakan \n1. Celcius ke fahrenheit \n2. Fahrenheit ke Celcius \ne. Keluar")

while True :
    memilih()
    pilihan = input("Masukkan Pilihan : ")
    if pilihan == '1' :
        ubahF()
    elif pilihan == '2' :
        ubahC()
    elif pilihan == 'e' :
        exit()
    else :
        print("Input Anda tidak tersedia pada daftar.")