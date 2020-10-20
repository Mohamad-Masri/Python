from tkinter import *

def paint (event):
	color = "red"
	x1,y1 = (event . x- 1 ), (event.y-1)
	x2,y2 = (event . x+ 1 ), (event.y+1)
	c.create_oval (x1,y1,x2,y2,fill = color, outline = color)

master = Tk()
master.title("Painting Programme")

c = Canvas (master, width = 600, height = 450, bg = "White")

c.pack(expand = YES, fill = BOTH)
c.bind('<B1-Motion>' ,paint)

message = Label (master, text = 'press and drag to draw')
message.pack(side= BOTTOM)
master.mainloop()
