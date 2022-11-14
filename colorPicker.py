from tkinter import *

scrn = Tk()
scrn.geometry("600x400")

def tryChange():
    try:
        colorCode()
    except:
        errorLabel.config(text="Length must be 6 characters")
        errorLabel.grid(row=2, column=2)

def colorCode():
    if len(colorEntry.get()) == 6:
        scrn.config(bg=("#" + colorEntry.get()))
        errorLabel.grid_forget()
    else:
        raise ValueError("Length must be 6 characters")

colorLabel = Label(text="Color Code:")
colorLabel.grid()

errorLabel = Label()

colorEntry = Entry()
colorEntry.grid(row=0, column=1)

changeBut = Button(text="Submit", command=tryChange)
changeBut.grid(row=1, column=1)

scrn.mainloop()