# imports
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock - Tech with Aenosh')
# root.geometry("600x600")


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('Calibri', 40, 'bold'),
            background='black',
            foreground='blue',
            )
lbl.pack(anchor='center')
time()
root.mainloop()
