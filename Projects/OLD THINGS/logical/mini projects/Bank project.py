money = 1000
print ('============> Welcome to Mouhamad AIM service banking <============')
enter_pin = int(input('enter you pin code : '))
while enter_pin == 5735 :
    Check_account = ('1. Check account')
    Withdraw_cash = ('2. Withdraw cash')
    Quit = ('3. Quit')
    money = money
    Amount = 0

    print (Check_account)
    print(Withdraw_cash)
    print(Quit)

    chose_num = int(input('Chose from the menu : '))

    if chose_num == 2:

        Amount = int(input('enter the amount : '))
        money = money - Amount
        print ('Now,you have :', money, '$')

    if chose_num == 1:
            print('you have', money, '$')
    if chose_num == 3:
        print('ok, Bye bye')

    print('_________________________')
else: print('pleae enter a valide pin code')