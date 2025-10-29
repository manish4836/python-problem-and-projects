class BankAccount:
    def __init__(self, Account_holder, initial_balance = 0):
        self.account_holder = Account_holder
        self.__balance = initial_balance
        self.account_number = f"Account: {id(self)}"

        print(f"Account created for {self.account_holder}")
        print(f"Initial balance: ${self.__balance}")
    

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Ammount Deposited: ${amount}")
            print(f"New Balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Insufficient funds. Current balance: ${self.__balance}")
        elif amount <= 0:
            print("withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Amount withdrawn: ${amount}")
            print(f"New Balance: ${self.__balance}")
    
    def get_balance(self):
        return self.__balance

account1 = BankAccount("Manish Yelne")
account1.deposite(5000)
account1.withdraw(2000)
account1.get_balance()

current_balance = account1.get_balance()
print(f"Account Holder: {account1.account_holder}")
print(f"Account Number: {account1.account_number}")
print(f"Current Balance: ${current_balance}")