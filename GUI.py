# import the necessary GUI library (tkinter)

from tkinter import *

from tkinter import ttk

# creating the instance of the Tk class

root = Tk()

frm = ttk.Frame(root, padding =10)

frm.grid()

ttk.Button(frm, text ="1", value = '1').grid(column =0, row = 0)

# loop to put everything on display until programme termination 

root.mainloop()