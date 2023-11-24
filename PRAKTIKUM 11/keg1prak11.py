from tkinter import Tk, Label, Entry, Button
my = Tk(className = "data Diri")

L0 = Label(my, text="Data Diri", font = ("Arial", 25))
L0.grid(row=0,column=0)
L1 = Label (my, text = "Nama", font = ("Arial", 10))
L1.grid(row=1,column=0)                                        
E1 = Entry(my)
E1.grid(row=1,column=1)
L2 = Label (my, text = "NIM", font = ("Arial", 10))
L2.grid(row=2,column=0)                                        
E2 = Entry(my)
E2.grid(row=2,column=1)
L1 = Label (my, text = "Buku favorit", font = ("Arial", 10))
L1.grid(row=3,column=0)                                        
E1 = Entry(my)
E1.grid(row=3,column=1)
L1 = Label (my, text = "Idola di kalangan sahabat", font = ("Arial", 10))
L1.grid(row=4,column=0)                                        
E1 = Entry(my)
E1.grid(row=4,column=1)
L1 = Label (my, text = "Motto", font = ("Arial", 10))
L1.grid(row=5,column=0)                                        
E1 = Entry(my)
E1.grid(row=5,column=1)

def tutup() :
    my.quit()

    
b = Button(my,text="Tutup", command = tutup)
b.grid(row=7,column=1)
my.mainloop()
