from tkinter import *
from PIL import ImageTk, Image
print("\033[H\033[J")
mainWindow = Tk()
x = 0

imgFrame = Frame(width = 63, height = 88)
imgFrame.grid(column=1, row=1)
zack = ImageTk.PhotoImage(Image.open("zack.jpeg"))
amish = ImageTk.PhotoImage(Image.open("amish.jpeg"))
jerma = ImageTk.PhotoImage(Image.open("jerma.jpeg"))
femboy = ImageTk.PhotoImage(Image.open("femboy.jpeg"))
imgList = [amish, femboy, zack, jerma]
imgLabel = Label(imgFrame, image=amish)
imgLabel.grid(column=1, row=1)
def forward():
    global x
    x = x + 1
    imgLabel.config(image=imgList[x])
    if x == 4:
        x = 0

def back():
    global x
    x = x - 1
    imgLabel.config(image=imgList[x])
    if x == 0:
        x = 4

backBut = Button(text="<", command=back)
backBut.grid(column=0, row=1)
forwardBut = Button(text='>', command=forward)
forwardBut.grid(column=2, row=1)

mainWindow.mainloop()