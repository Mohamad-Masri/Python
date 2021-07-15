from tkinter import  *
import os


creds = 'tempfile.temp'

def F():

    r = Tk()
    r.title(':D')
    r.geometry('150x50')
    rlbl = Label(r, text="hello, " + name.get())
    rlbl.pack()
    r.mainloop()


def tt():

    global F
    global root1
    global name


    root1 = Tk()
    root1.title("Hello")

    ff= Label(root1, text="")
    ff.grid(row=2, column=0)

    ffg = Label(root1, text="")
    ffg.grid(row=4, column=0)

    intruction = Label(root1, text='Hello, please enter your name :')
    intruction.grid(row=0, column=0, sticky=E)

    name = Entry(root1)
    name.grid(row=3, column=2)

    nameE1 = Label(root1, text='your name:')
    nameE1.grid(row=3, column=0, sticky=W)

    enterB = Button(root1, text='enter', command = F)
    enterB.grid(row=5, column=3, sticky=W)

    root1.mainloop()

tt()