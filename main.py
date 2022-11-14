from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

mainWindow = Tk()
var = IntVar()
R1 = Radiobutton(mainWindow, text="Option 1", variable=var, value=1, command=sel)
R1.pack()

R2 = Radiobutton(mainWindow, text="Option 2", variable=var, value=2, command=sel)
R2.pack()

R3 = Radiobutton(mainWindow, text="Option 3", variable=var, value=3, command=sel)
R3.pack()

label = Label(mainWindow)
label.pack()
mainWindow.mainloop()