class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
        print(f"New Account created by Name: {self.account_holder}")

    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"Amount is successfully deposited: {amount}")
            print(f"New balance: {self.balance}")
        else: 
            print(f"Deposite amount must be positive")
            
    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficient fund. Current Balance: {self.balance}")
        elif amount < 0:
            print(f"Withdraw amount must be positive amount.")
        else:
            self.balance -= amount
            print(f"Withdraw successfully: {amount}")
            print(f"New Balance: {self.balance}")

    def check_balance(self):
        print(f"Name: {self.account_holder}")
        print(f"Available Balance: {self.balance}")

account1 = BankAccount("manish yelne",1000)
account2 = BankAccount("Aarav",500)

print(account1.check_balance())
print(account2.check_balance())

print("\n" + "="*30)

account2.deposit(1000)
account2.withdraw(800)  
account2.withdraw(1000) 
account2.check_balance()