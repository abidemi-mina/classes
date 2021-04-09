class Budget():
    

    # def __init__(self,deposit,withdraw,inputing,balances):
    #     self.d = deposit
    #     self.w = withdraw
    #     self.i = inputing
    #     self.b = balances

    def result(self):
        deposit = int(input('How much do you want to deposit :'))
        print(f'You have deposited {deposit} naira in this category')
        withdraw = int(input('how much do you want to withdraw :'))
        print(f'You have withdrawed {withdraw} naira from this category')
        balance = deposit - withdraw 
        print(f'Your remaining balance is  , {balance} naira ')



print('1 . Food ')
print('2 . Clothing ')
print('3 . Entertainment ')
request = int(input('What do you want to budget for :'))
if request == 1 :

    Food = Budget()
    Food.result()

elif request == 2 :

    Clothing = Budget()
    Clothing.result()

elif request == 3 :

    Entertainment = Budget()
    Entertainment.result()

else :
    print ('choose a valid option')







