# Bank Account System 
# Requirements:
# Deposit
# Withdraw
# Check Balance


class BankAccount:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient Balance")

    def display(self):
        print(self.balance)

account=BankAccount("Ali",5000)

account.deposit(1000)
account.withdraw(2000)
account.display()