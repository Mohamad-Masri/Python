lter_none
edit
play_arrow

brightness_4
import fbchat 
from getpass import getpass 
username = str(raw_input("Username: ")) 
client = fbchat.Client(username, getpass()) 
no_of_friends = int(raw_input("Number of friends: ")) 
for i in xrange(no_of_friends): 
    name = str(raw_input("Name: ")) 
    friends = client.getUsers(name)  # return a list of names 
    friend = friends[0] 
    msg = str(raw_input("Message: ")) 
    sent = client.send(friend.uid, msg) 
    if sent: 
        print("Message sent successfully!")
