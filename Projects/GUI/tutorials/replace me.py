import tkinter as tk

def replace_btn_text():
    b['text'] = e.get()

root = tk.Tk()

e = tk.Entry(root)
b = tk.Button(root, text="Replace me!", command=replace_btn_text)

e.pack()
b.pack()
root.mainloop()