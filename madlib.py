from tkinter import *
scrn = Tk()
scrn.geometry("600x400")

nounLabel = Label(text="Noun")
nounLabel.grid(row=1, column=0)

nounEntry = Entry()
nounEntry.grid(row=0, column=0)

adjectiveLabel = Label(text="Adjective")
adjectiveLabel.grid(row=1, column=1)

adjectiveEntry = Entry()
adjectiveEntry.grid(row=0, column=1)

personLabel = Label(text="Person")
personLabel.grid(row=1, column=2)

personEntry = Entry()
personEntry.grid(row=0, column=2)

colorLabel = Label(text="Color")
colorLabel.grid(row=1, column=3)

colorEntry = Entry()
colorEntry.grid(row=0, column=3)

adverbLabel = Label(text="Present Verb")
adverbLabel.grid(row=1, column=4)

adverbEntry = Entry()
adverbEntry.grid(row=0, column=4)

madlibLabel = Label()
madlibLabel.grid(row=3)

def create(adjective, noun, person, color, adverb):
    madlibLabel.config(text= "A " + adjective + " " + person + " was " +  adverb + " down the " + color + " " + noun + ".")

submitBut = Button(text = "    Submit    ", command=lambda:create(adjectiveEntry.get(), nounEntry.get(), personEntry.get(), colorEntry.get(), adverbEntry.get()))
submitBut.grid(row=2)

scrn.mainloop()