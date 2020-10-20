import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()


#showinfo()
#showwarning()
#showerror ()
#askquestion()
#askokcancel()
#askyesno ()
#askretrycancel ()
