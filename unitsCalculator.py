from tkinter import *

scrn = Tk()

def fcFunc():
    outputLabel.config(text=int(fcEntry.get()) * (9/5) + 32)

def miFunc():
    outputLabel.config(text=int(miEntry.get()) * 100)

def pkgFunc():
    outputLabel.config(text=int(pkgEntry.get()) * 0.4536)

def deFunc():
    outputLabel.config(text=int(deEntry.get()) * 0.97)

fcLabel = Label(text="Fahrenheit to Celcius | ")
fcLabel.grid(column=0, row=0)
fcEntry = Entry()
fcEntry.grid(column=0, row=1)
fcCalc = Button(text="Calculate", command=fcFunc)
fcCalc.grid(column=0, row=2)

miLabel = Label(text="Millimeters to Centimeters | ")
miLabel.grid(column=1, row=0)
miEntry = Entry()
miEntry.grid(column=1, row=1)
miCalc = Button(text="Calculate", command=miFunc)
miCalc.grid(column=1, row=2)

pkgLabel = Label(text="Pounds to Kilograms | ")
pkgLabel.grid(column=2, row=0)
pkgEntry = Entry()
pkgEntry.grid(column=2, row=1)
pkgCalc = Button(text="Calculate", command=pkgFunc)
pkgCalc.grid(column=2, row=2)

deLabel = Label(text="Dollars to Euros ")
deLabel.grid(column=3, row=0)
deEntry = Entry()
deEntry.grid(column=3, row=1)
deCalc = Button(text="Calculate", command=deFunc)
deCalc.grid(column=3, row=2)

outputLabel = Label(text="")
outputLabel.grid(row=3)

scrn.mainloop()