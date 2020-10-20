from tkinter import *


def get_variable_value():
    valueresult.set( strlname.get() + ' ' + strfname.get() ) #assign val variable to other
    print(valueresult.get()) #if you want see the result in the console


root = Tk()

strfname = StringVar()
strlname = StringVar()
valueresult = StringVar()

labelf = Label(root, text = 'First Name').pack()
fname = Entry(root, justify='left', textvariable = strfname).pack() #strlname get input 

labell = Label(root, text = 'Last Name').pack()
lname = Entry(root, justify='left', textvariable = strlname).pack() #strfname get input 

button = Button(root, text='Show', command=get_variable_value).pack()
res = Entry(root, justify='left', textvariable = valueresult).pack() #only to show result


root.mainloop()
