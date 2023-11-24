import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("400x600")

def close() :
    root.destroy()

tk.Label(root, text="Data Diri", font=("Times New Roman", 24)).place(x=10)
tk.Label(root, text="Nama", font=("Times New Roman", 10)).place(x=10,y=40)
Label(root,text="Inandra Asha Fardhana", font=("Times New Roman", 10)).place(x=160,y=40)
Label(root,text="NIM", font=("Times New Roman", 10)).place(x=10, y=70)
Label(root,text="L200220045", font=("Times New Roman", 10)).place(x=160,y=70)
Label(root,text="Buku Favorit", font=("Times New Roman", 10)).place(x=10, y=100)
Label(root,text="Berani Tidak Disukai", font=("Times New Roman", 10)).place(x=160,y=100)
Label(root,text="Idola di kalangan sahabat", font=("Times New Roman", 10)).place(x=10, y=130)
Label(root,text="Ali bin Abi Thalib", font=("Times New Roman", 10)).place(x=160,y=130)
Label(root,text="Motto", font=("Times New Roman", 10)).place(x=10, y=160)
Label(root,text="Masalah adalah sumber kekuatan", font=("Times New Roman", 10)).place(x=160,y=160)

Button(root,text="Tutup", font=("Times New Roman", 10), command=close, height=2,width=13).place(x=160,y=190)

root.mainloop()