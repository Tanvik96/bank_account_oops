class BalanceException(Exception):
    pass





class BankAccount:
    def __init__ (self, initialamount,name):
        self.balance = initialamount
        self.name = name
        print(f"\nAccount'{self.name}' created.\nBalance = ₹{self.balance:.2f}")

    def getbalance(self):
        print(f"\nAccount'{self.name}' Balance = ₹{self.balance:.2f}")

    def deposit(self,amount):
        self.balance= self.balance + amount
        print("Deposit Completed")
        self.getbalance()

    # def withdraw(self,amount):
    #     if self.balance < amount:
    #         print("Insufficient Balance")
    #     else:
    #         self.balance -= amount
    #         print(f" The amount ₹{amount} is withdraw")
    #         self.getbalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else: 
            raise BalanceException(f"\nSorry! account '{self.name}' only has a balance of ₹{self.balance:.2f}")
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f" The amount ₹{amount} is withdraw")
            self.getbalance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")
        
        

    def transfer(self,amount,account):
        try:
            print('\n**********\n\n Beginning Transfer...')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n Transfer complete! \n\n**********")
        except BalanceException as error:
            print(f"\n Transfer interrupted... {error}")



class InterestRewardsAcct(BankAccount):
    def deposit(self,amount):
        self.balance += (amount*1.05)
        print("Deposit Completed ")
        self.getbalance()

class SavingAcct(InterestRewardsAcct):
    def __init__(self,initialamount,name):
        super().__init__(initialamount, name)
        self.fee = 5

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount +self.fee)
            self.balance -= (amount + self.fee)
            print("\n Withdraw Completed.")
            self.getbalance()
        except BalanceException as error:
            print(f"\n Withdraw Interrupted: {error}")