import map_1
import map_2
import map_3
from Tkinter import *
import random

def map1():
    map_1.a_function()

def map2():
    map_2.a_function()

def map3():
    map_3.a_function()

def main_funct():
    root = Tk()
    root.geometry("350x400+30+30")
    topFrame = Frame(root)
    topFrame.pack(side=TOP)

    #variables used in the starting of the program
    TFrame = Frame(root)
    TFrame.pack()

    intro = Label(topFrame, text="DM Helper Tool")
    intro.pack()

    mapBut1 = Button(topFrame,text='Do the thing',command=map1)
    mapBut1.pack()

    mapBut2 = Button(topFrame,text='Do the thing',command=map2)
    mapBut2.pack()

    mapBut3 = Button(topFrame,text='Do the thing',command=map3)
    mapBut3.pack()


    closeBut = Button(topFrame,text="Close",command=root.destroy)
    closeBut.pack(side=BOTTOM)

    root.mainloop()
    print 'hopefully...'



if __name__ == '__main__':
    main_funct()
