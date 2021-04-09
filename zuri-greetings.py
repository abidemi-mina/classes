# greetings =  ("Hello World")
# print(greetings)
# def f():
    
#     print (s)

    name = input('enter your account name :')
    password = input('enter your password :')
    
    if not name:
        print ('   Incorrect input , try again ')
    else:
        print ('Login succesful')
        import datetime
        date =datetime.datetime.now()
        print(f' Login in details {date} ')

        print('These are the services we render , please kindly choose an option')
        print(" 1. Withdrawal")
        print(" 2. Deposit")
        print(" 3. Comlpaints") 
        options = int(input('Select an option : '))
        if(options == 1):
            option1 = input('How much would you like to withdraw :')
            print('Take your cash')
        elif (options == 2):
            option2 = int(input('How much will you like to deposit: '))
            balance = float(option2 + 50000)
            print(f'Your current balance is {balance}')
        elif(options == 3):
            complaint = input('What issue will you like to report :')
            print("Thank you for contacting us")
        else :
            print('Invalid option selected')
# s = 'I Love Python'
# f()









