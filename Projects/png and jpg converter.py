from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd #It will contain open and save dialog boxes

'''Functions which are being used in the program (To convert JPG to PNG and Vice Versa)'''
def jpgtopng():
    root.config(bg='#badc57')
    def getjpgfile():
        global pic
        file_path = fd.askopenfilename()
        pic=Image.open(file_path)   #It will open the file and will store it in pic variable (.open and .save are the methods of Image of PIL Module)
        
    def savepngfile():
        global pic
        export_file_path = fd.asksaveasfilename(defaultextension='.png',filetypes= [('Image (.png file)','.png')] )
        pic.save(export_file_path)      #It will save the file to the specified path
        
    global Head
    imagelabel.destroy()
    f1.destroy()
    Head.destroy()
    Head=Label(text='JPG To PNG Converter',font='Lucida 20 bold',bg='black',fg='#F4C724',padx=5,pady=5)
    Head.pack(pady=10)
    #To get jpg file
    browse_jpg = Button(text="      Import JPG File     ", bg='#BB2CD9', fg='white', font=('helvetica', 15, 'bold'),command=getjpgfile)
    browse_jpg.pack(pady=20)
    #To save jpg file
    save_jpg=Button(text='  Convert JPG To PNG  ', bg='#BB2CD9', fg='white', font=('helvetica', 15, 'bold'),command=savepngfile)
    save_jpg.pack(pady=10)
    
    #Image in bottom
    bottom_pic=Image.open('Images/jtop.jpg')
    bottom_pic=bottom_pic.resize((400,250),Image.ANTIALIAS)
    bg_pic=ImageTk.PhotoImage(bottom_pic)
    img_label=Label(root,image=bg_pic)
    img_label.image=bg_pic  #It will make a reference or keep a reference
    img_label.pack(side=BOTTOM,pady=40)

    #Close Button
    close=Button(text='Close',command=root.destroy,bg='black',fg='white',font='11')
    close.place(x=205,y=422)

    

def pngtojpg():
    root.config(bg='#67E6DC')
    def getpngfile():
        global pic
        file_location=fd.askopenfilename()
        pic=Image.open(file_location)       #It will store the selected file in pic variable 
        pic=pic.convert('RGB')  #It will covert the file from RGBA to RGB coz PNG files have some transparency or alpha value so we need to remove that to make it a JPG file.
        
    def savejpgfile():
        global pic
        export_file_location = fd.asksaveasfilename(defaultextension='.jpg')
        pic.save(export_file_location)  #It will save the image to a specified location
        
    global Head
    imagelabel.destroy()
    f1.destroy()
    Head.destroy()
    Head=Label(text='PNG To JPG Converter',font='Lucida 20 bold',bg='black',fg='#F4C724',padx=5,pady=5)
    Head.pack(pady=10)
    #To get jpg file
    browse_jpg = Button(text="      Import PNG File     ", bg='#2B2B52', fg='white', font=('helvetica', 15, 'bold'),command=getpngfile)
    browse_jpg.pack(pady=20)
    #To save jpg file
    save_jpg=Button(text='  Convert PNG To JPG  ', bg='#2B2B52', fg='white', font=('helvetica', 15, 'bold'),command=savejpgfile)
    save_jpg.pack(pady=10)

    #Image in bottom
    bottom_pic=Image.open('Images/ptoj.jpg')
    bottom_pic=bottom_pic.resize((400,250),Image.ANTIALIAS)
    bg_pic=ImageTk.PhotoImage(bottom_pic)
    img_label=Label(root,image=bg_pic)
    img_label.image=bg_pic  #It will make a reference or keep a reference
    img_label.pack(side=BOTTOM,pady=40)

    #Close Button
    close=Button(text='Close',command=root.destroy,bg='black',fg='white',font='11')
    close.place(x=205,y=422)

''' Events of buttons '''
def jtopenter(event):
    jtop.config(bg='black',fg='white')
def jtopleave(event):
    jtop.config(bg='white',fg='black')

def ptojenter(event):
    ptoj.config(bg='black',fg='white')
def ptojleave(event):
    ptoj.config(bg='white',fg='black')

    
'''Main GUI Program'''

root=Tk()
root.title('Image Converter')
#root.wm_iconbitmap('Images/icon/pic.ico')
root.geometry('450x480')


'''Creating Main Window :'''

#Heading of GUI
Head=Label(text='Image Converter',font='Lucida 20 bold',bg='black',fg='#F4C724',padx=5,pady=5)
Head.pack(pady=10)

#Buttons
f1=Frame(root)
jtop=Button(f1,text='JPG To PNG',font='arial 15 bold',command=jpgtopng)
jtop.pack(side='left',padx=40)
jtop.bind('<Enter>',jtopenter)
jtop.bind('<Leave>',jtopleave)
ptoj=Button(f1,text='PNG To JPG',font='arial 15 bold',command=pngtojpg)
ptoj.pack(padx=40)
ptoj.bind('<Enter>',ptojenter)
ptoj.bind('<Leave>',ptojleave)
f1.pack(pady=20)

#Image
#img=Image.open('img.png')
img=img.resize((300,275),Image.ANTIALIAS)
bgpic=ImageTk.PhotoImage(img)
imagelabel=Label(image=bgpic)
imagelabel.pack(pady=10)

#Status Bar
sbar=Label(text='By Logical Coder',font='Helvetica 10 bold',relief=SUNKEN,anchor='w',padx=10)
sbar.pack(side=BOTTOM,fill=X)


root.mainloop()