from tkinter import *

window = Tk()
window.title("Kalkulator Sederhana")
window.geometry("200x200")

lbl = Label(window, text = "Angka 1")
lbl.grid(column=1, row=0)

nilai1 = Entry(window,width=10)
nilai1.grid(column=2,row=0)

label2 = Label(window, text = "Angka 2")
label2.grid(column=1, row=1)

nilai2 = Entry(window,width=10)
nilai2.grid(column=2,row=1)

label3 = Label(window, text = "Hasil = ")
label3.grid(column=0, row=5)

hasil = Label(window,width=10)
hasil.grid(column=1,row=5)

def tambah() :
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))

def kurang() :
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))

def kali() :
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))

def bagi() :
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))


btn = Button(window, text="+", command=tambah)
btn.grid(column=0, row=3)

btn = Button(window, text="-", command=kurang)
btn.grid(column=1, row=3)

btn = Button(window, text="x", command=kali)
btn.grid(column=2, row=3)

btn = Button(window, text=":", command=bagi)
btn.grid(column=3, row=3)

window.mainloop()
