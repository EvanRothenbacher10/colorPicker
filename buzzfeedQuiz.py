from tkinter import *
from PIL import ImageTk, Image
scrn = Tk()
scrn.geometry("600x400")

scores = [0, 0, 0, 0]
highscore = 0
finAns = 0
quesLabel = Label(text="Welcome to the Taco Bell quiz!")
quesLabel.grid(row=0)
nameList = ["Amish", "Femboy", "Mr. Patrowski", "jerma"]
x = 0

def ques1():
    global scores   
    scores = [0, 0, 0, 0]
    quesLabel.config(text="How much blahaj blast")
    imgLabel.grid_forget()
    R1.config(text="1")
    R2.config(command="", text="1")
    R3.config(text="2")
    R4.config(text="4")
    R1.grid(row=1)
    R2.grid(row=2)
    R3.grid(row=3)
    R4.grid(row=4)
def ques2():
    quesLabel.config(text="A train leaves the station at 10:45 PM,\n and arrives at its destination at 2 AM the next day \n(without changing time zones). The train was stopped for 1/2 houor while it had engine trouble;\n the rest of the time, its average speed was 80 miles per hour. \nWhat total distace did the train travel?")
    R1.config(text="De-rail the train")
    R2.config(text="140 Miles")
    R3.config(text="220 Miles")
    R4.config(text="240 Miles")
def ques3():
    quesLabel.config(text="Top 10 streamers")
    R1.config(text="Ninja Fortnite")
    R2.config(text="Ludwig Mogul Bethooven")
    R3.config(text="Jerma Ablertson")
    R4.config(text="Sodapoppin")
def ques4():
    quesLabel.config(text="The Industrial Revolution and its Consquences\n is written by who?")
    R1.config(text="Joooo Biden")
    R2.config(text="Josh Powell")
    R3.config(text="Theodore John Kaczynski")
    R4.config(text="Jerma Albertson")
def ques5():
    quesLabel.config(text="Which country has the hottest males?")
    R1.config(text="Japan")
    R2.config(text="Korea")
    R3.config(text="Sweden")
    R4.config(text="Poland")
def ques6():
    global Img
    highscore = max(scores)
    finAns = scores.index(highscore)
    imgLabel.config(image=imgList[finAns])
    quesLabel.config(text="You got :" + nameList[finAns])
    imgLabel.grid()
    R1.config(text="Restart")
    R2.grid_forget()
    R3.grid_forget()
    R4.grid_forget()

questions = [ques1, ques2, ques3, ques4, ques5, ques6]

def calc():
    global x
    scores[int(var.get())] = scores[int(var.get())] + 1
    print(scores[int(var.get())])
    questions[x]()
    x = x + 1
    if x == 6:
        x = 0


var = IntVar()
R1 = Radiobutton(scrn, text="Start", variable=var, value=0)
R1.grid()

R2 = Radiobutton(scrn, text="Quit", variable=var, value=1, command=lambda:scrn.destroy())
R2.grid()

R3 = Radiobutton(scrn, text="2", variable=var, value=2)

R4 = Radiobutton(scrn, text="4", variable=var, value=3)

submitBut = Button(text='Submit', command=calc)
submitBut.grid(row=5)

imgFrame = Frame(width = 63, height = 88)
imgFrame.grid(row=6)
zack = ImageTk.PhotoImage(Image.open("zack.jpeg"))
amish = ImageTk.PhotoImage(Image.open("amish.jpeg"))
jerma = ImageTk.PhotoImage(Image.open("jerma.jpeg"))
femboy = ImageTk.PhotoImage(Image.open("femboy.jpeg"))

imgList = [amish, femboy, zack, jerma]



imgLabel = Label(imgFrame, image=zack)



scrn.mainloop()