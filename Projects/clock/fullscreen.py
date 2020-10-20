#  =====================================================
#   ppppppppppppp      
#   ppppppppppppppp     pppppp                   ppppppp
#   ppppp       pppp    pppppp                   ppppppp
#   ppppp       pppp    pppppp                   ppppppp
#   ppppp       pppP    pppppp                   ppppppp
#   ppppp      pppp     pppppp         p         ppppppp
#   ppppppppppppp       pppppp        ppp        ppppppp
#   pppppppppp          pppppp       ppppp       ppppppp
#   ppppp               pppppp      ppp ppp      ppppppp
#   ppppp               pppppp     ppp   ppp     ppppppp
#   ppppp               pppppp    ppp     ppp    ppppppp
#   ppppp               pppppppppppp       ppppppppppppp
#   ppppp               ppppppppppp         ppppppppppp

#  Youtube => Programmers World
#  Instagram => @programmer_py
#  Facebook => Programmers World
#  Welcome all to Programming With Python
#  =====================================================

from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

def quit(*args):
    main.destroy()

def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%H:%M:%S"))
    txt.set(time)
    main.after(1000, clock_time)


main = Tk()
main.attributes("-fullscreen", True)
main.configure(background="black")
main.bind("x", quit)
main.after(1000, clock_time)

fnt = font.Font(family='Helvetica', size=120, weight='bold')
txt = StringVar()
lbl = ttk.Label(main, textvariable=txt, font=fnt, foreground='white', background='black')
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

main.mainloop()
