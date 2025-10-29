class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.__balance = balance
        self.account_number = f"ACC{id(self)}"

        print(f"New Account created: {account_holder}")

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Ammount Deposited: {amount}")
            print(f"New Balance: {self.__balance}")
        else:
            print(f"Deposite Amount must be positive.")
        
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Insufficient fund. Current Balance: {self.__balance}")
        elif amount < 0:
            print(f"Please Amount must be Positive.")
        else:
            self.__balance -= amount
            print(f"Amount Withdraw: {amount}")
            print(f"New Balance: {self.__balance}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.__balance}")

account1 = BankAccount("manish yelne", 10000)
account2 = BankAccount("Aarav doye", 5000)


account1.deposit(2000)
account1.withdraw(1500)
account1.display_balance()

account2.deposit(500)
account2.withdraw(20000)
account2.withdraw(500)
account2.display_balance()