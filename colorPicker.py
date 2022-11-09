from tkinter import *
scrn = Tk()
scrn.geometry("600x400")
scrn.config(bg="#654654")

colorLabel = Label(text="Color Code:")
colorLabel.grid()

colorEntry = Entry()
colorEntry.grid(row=0, column=1)

changeBut = Button(text="Submit")
changeBut.grid(row=1, column=1)

def colorCode():
    cC = "#" + colorEntry.get()
    print(cC)

scrn.mainloop()