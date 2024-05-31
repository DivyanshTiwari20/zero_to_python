'''Question: Create a class BankAccount with private attributes __balance. Provide methods to deposit and withdraw money, and to check the balance.'''

class BankAccount():
    def __init__(self,balance=0):
        self.__balance=balance

    def deposite(self,amount):
        self.__balance += amount
    
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance-=amount

        else:
            print("Incificent balance")

    def checkBalance(self):
        return self.__balance
    
account=BankAccount()
account.deposite(500)
account.withdraw(700)
print(account.checkBalance())

