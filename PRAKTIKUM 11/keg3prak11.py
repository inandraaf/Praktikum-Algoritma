from tkinter import *

my = Tk(className="Menghitung Luas Limas Segitiga")

L = Label(my, text="Bangun Geometri", font=("Arial", 14))
L.grid(row=0,column=0,columnspan=1)
L1 = Label(my, text="Limas segi empat adalah bangun ruang sejenis limas yang mempunyai alas segi empat, bisa berupa persegi, persegi panjang, belah ketupat, layang-layang, jajar genjang, atau trapesium.")
L1.grid(row=1,column=0,columnspan=1)

A1 = Label(my, text= "Alas : ")
A1.grid(row=2,column=0)

a1 = Entry(my,width=20)
a1.grid(row=2,column=1)

T1 = Label(my,text="Tinggi : ")
T1.grid(row=4,column=0)

a2 = Entry(my,width=20)
a2.grid(row=4,column=1)

Luas = Label(my, text="0")
Luas.grid(column=1, row=5)

def Limas() :
    Luas.configure(text=(int(4*(0.5*int(a1.get())*int(a2.get())))+(int(a1.get())*int(a1.get()))))

btn = Button(my, text="Hitung Luas", command=Limas)
btn.grid(row=5,column=0)

my.mainloop()