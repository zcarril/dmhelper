from Tkinter import *
import random
import belowDeck


def aboveAndBelow():
    belowDeck.a_function()

def a_function():
    root = Toplevel()
    root.geometry("1220x720+30+30")

    #making image as the backround (must be in GIF format)
    bg_image = PhotoImage(file="C:\\Users\\zac\\Desktop\\dmHelper\\images\\shipProfile.GIF")
    backround_label = Label(root,image=bg_image)
    backround_label.place(x=0, y=0, relwidth=1, relheight=1)

    #description labels
    intro = Label(root, text="The Ship Home")
    intro.place(x=600,y=50, in_=root)


    #widgetts (sets/creates them)
    button1 = Button(root,command=aboveAndBelow,text="Below Deck",fg="white", bg="black")
    button2 = Button(root,command=aboveAndBelow,text="Above Deck",fg="white", bg='black')

    #...and then display them(will "pack" on top innately)
    button1.place(x=600,y=450, in_=root)
    button2.place(x=600,y=350, in_=root)

    #keep it open and goes at the bottom
    root.mainloop()

if __name__ == '__main__':
    a_function()
