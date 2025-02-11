# import the necessary GUI library (tkinter)

from tkinter import *

from tkinter import ttk

# creating the instance of the Tk class

root = Tk()

frm = ttk.Frame(root, padding =10)

frm.grid()

ttk.Button(frm, text ="1").grid(column =0, row = 0)
ttk.Button()

# loop to put everything on display until programme termination 

root.mainloop()



''' Proposed planning 

In my mind to allow more complex calculations I need to assign values to the tkinter buttons and then append them to a string using a callback function

This can then be typecast to an integer and used for calculations 

if I want to extend the complexity further to more than two numbers, more than one operand, there will need to be logic for initialising a new variable each time an operand is clicked 

I should add the explicit click of an equals button as an endpoint this will make programming the calculation point easier 

'''

 