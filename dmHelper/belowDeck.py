from Tkinter import *
import random

def a_function():
    root = Toplevel()
    root.geometry("1600x800+30+30")

    #making image as the backround (must be in GIF format)
    bg_image = PhotoImage(file="C:\\Users\\zac\\Desktop\\dmHelper\\aboveAndBelow.GIF")
    backround_label = Label(root,image=bg_image)
    backround_label.place(x=0, y=0, relwidth=1, relheight=1)


    #widgetts (sets/creates them)
    button0 = Button(root,text="test0",fg="white",bg="black")
    button1 = Button(root,text="test1",fg="white", bg="black")
    button2 = Button(root,text="test2",fg="white", bg='black')
    button3 = Button(root,text="test3",fg="white", bg='black')
    button4 = Button(root,text="test4",fg="white", bg='black')
    button5 = Button(root,text="test5",fg="white", bg='black')
    button6 = Button(root,text="test 6",fg="white", bg='black')


    #...and then display them(will "pack" on top innately)
    button0.place(x=200,y=200, in_=root)
    button1.place(x=400,y=200, in_=root)
    button2.place(x=800,y=200, in_=root)
    button3.place(x=1200,y=200, in_=root)
    button4.place(x=400,y=600, in_=root)
    button5.place(x=800,y=600, in_=root)
    button6.place(x=1200,y=600, in_=root)

    #keep it open and goes at the bottom
    root.mainloop()

if __name__ == '__main__':
    a_function()