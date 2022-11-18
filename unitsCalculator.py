from tkinter import *

scrn = Tk()

def fcFunc():
    print(fcEntry.get() * (9/5) + 32)
    outputLabel.config(text=str(fcEntry.get() * (9/5) + 32))
    
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
miCalc = Button(text="Calculate")
miCalc.grid(column=1, row=2)

pkgLabel = Label(text="Pounds to Kilograms | ")
pkgLabel.grid(column=2, row=0)
pkgEntry = Entry()
pkgEntry.grid(column=2, row=1)
pkgCalc = Button(text="Calculate")
pkgCalc.grid(column=2, row=2)

deLabel = Label(text="Dollars to Euros ")
deLabel.grid(column=3, row=0)
deEntry = Entry()
deEntry.grid(column=3, row=1)
deCalc = Button(text="Calculate")
deCalc.grid(column=3, row=2)

outputLabel = Label(text="")
outputLabel.grid(row=3)
scrn.mainloop()