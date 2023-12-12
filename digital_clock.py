from tkinter import *
from tkinter.ttk import *

from time import strftime
root =Tk()
root.title("clock")

def time():
    string =strftime('%H:%M:%S:%p')
    dati.config(text=string)
    dati.after(1000,time)

dati=Label(root,font=("dk-digital",80),background="green",foreground="white")
dati.pack(anchor='center')
time()

mainloop()