print('Hello user, please enter a valid user name and password')

username = input('enter your username: ')
password = input('enter your password: ')
password_verification = input('enter your password_verification: ')

if password_verification==password :

    print ('you have signed up succesfully, please login:')

    new_username = input('enter your username: ')
    new_password = input('enter your password: ')
    if new_password == password and new_username == username :
        print ('you have succesfully logined in')
    else:
        print("user name or password don't match")
else:
    print ('please enter a valid password.')
