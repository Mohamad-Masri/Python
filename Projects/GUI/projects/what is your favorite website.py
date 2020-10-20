import time
import webbrowser
from tkinter import *

root = Tk()

v = IntVar()
v.set(0)  # initialize the choice

choices = [
    ("Ethan Peacock",1),
    ("Google",2),
    ("Youtube",3),
    ("Twitter",4),
    ("Facebook",5),
    ("Instagram",6)
]

def ShowChoice():
    print(v.get())

    answer = v.get()

    if answer == 1:
        webbrowser.open("http://EthanPeacock.com")
    elif answer == 2:
        webbrowser.open("http://google.com")
    elif answer == 3:
        webbrowser.open("http://youtube.com")
    elif answer == 4:
        webbrowser.open("http://twitter.com")
    elif answer == 5:
        webbrowser.open("http://facebook.com")
    elif answer == 6:
        webbrowser.open("http://instagram.com")

Label(root,
      text="""Choose your favorite
  website:""",
      justify = LEFT,
      padx = 20).pack()

for text, value in choices:
    b = Radiobutton(root,
                    text=text,
                    indicatoron = 0,
                    width = 20,
                    padx = 20,
                    variable = v,
                    command=ShowChoice,
                    value = value).pack(anchor=W)

mainloop()
