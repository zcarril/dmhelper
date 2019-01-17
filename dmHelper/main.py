import theShip
import map_2
import map_3
from Tkinter import *
import random

def map1():
    theShip.a_function()

def map2():
    map_2.a_function()

def map3():
    map_3.a_function()

def main_funct():
    root = Tk()
    root.geometry("1200x900+30+30")



    #making image as the backround(must be in GIF format)
    bg_image = PhotoImage(file="C:\Users\zac\Desktop\dmHelper\mainBG.GIF")
    backround_label = Label(root,image=bg_image)
    backround_label.place(x=0,y=0,relwidth=1,relheight=1)

    topFrame = Frame(root)
    topFrame.pack(side=TOP)



    #variables used in the starting of the program
    #creation and placing of labels and buttons
    intro = Label(root, text="Field Trip with Vacco", fg="white", bg="black")
    intro.place(x=800,y=400, in_=root)


    mapBut1 = Button(root,text='The Ship',command=map1, fg="white", bg="black")
    mapBut1.place(x=800,y=440, in_=root)

    mapBut2 = Button(root,text='Do the thing',command=map2, fg="white", bg="black")
    mapBut2.place(x=800,y=480, in_=root)

    mapBut3 = Button(root,text='Do the thing',command=map3, fg="white", bg="black")
    mapBut3.place(x=800,y=520, in_=root)


    closeBut = Button(root,text="Close",command=root.destroy, fg="white", bg="black")
    closeBut.place(x=1100,y=20, in_=root)

    root.mainloop()
    print 'hopefully...'



if __name__ == '__main__':
    main_funct()
