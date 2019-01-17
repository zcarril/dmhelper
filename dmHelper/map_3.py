from Tkinter import *
import random


def a_function():
    root = Tk()
    root.geometry("350x400+30+30")
    
    #frames
    topFrame = Frame(root)
    topFrame.pack()

    btmFrame = Frame(root)
    btmFrame.pack(side=BOTTOM)

    #description labels
    intro = Label(topFrame, text="MAP NAME HERE")
    intro.pack()

    #widgetts (sets/creates them)
    button1 = Button(topFrame,text="NPC",fg="green")


    #...and then display them(will "pack" on top innately)
    button1.pack(side=BOTTOM)


    #keep it open and goes at the bottom
    root.mainloop()

if __name__ == '__main__':
    a_function()