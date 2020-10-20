import os

creds = 'tempfile.temp'

#----------------------------------------------------------------

#to del data from data base

def DelUser():
    os.remove(creds)  # Removes the file
    rootA.destroy()  # Destroys the login window
    Signup()


#----------------------------------------------------------------

#to save data in data base

def CheckLogin():
    with open(creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
		
#----------------------------------------------------------------



#to save data in data base

def FSSignup():
    with open(creds, 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.close()