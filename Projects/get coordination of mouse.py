import tkinter as tk
def getorigin(eventorigin):
      global x,y
      x = eventorigin.x
      y = eventorigin.y
      print(x,y)

root = tk.Tk()
root.bind("<Button 1>",getorigin)
