from tkinter import *
scrn = Tk()
scrn.geometry("600x400+50+50")

def calc():
    ansLabel = Label(text=(int(heightEntry.get()) * int(widthEntry.get())))
    ansLabel.grid(row=3, column=0)

widthLabel = Label(text="Width")
widthLabel.grid(row=0, column=0)

heightLabel = Label(text="Height")
heightLabel.grid(row=1, column=0)

heightEntry = Entry()
heightEntry.grid(row=0,column=1)

widthEntry = Entry()
widthEntry.grid(row=1,column=1)

calcButton = Button(text="Calculate", command=calc)
calcButton.grid(row=2, column=0)

scrn.mainloop()