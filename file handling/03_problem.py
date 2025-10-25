balance = 0

def deposite():
    global balance 
    try:
        amount = float(input("kitna paisa deposite karna hai: "))
        if amount <= 0:
            print("positive number enter karo!")
            return
        balance += amount
        print(f"{amount} deposite ho gaya. New Balance {balance}")
    except ValueError:
        print("Number enter karo, Text nahi!")

def withdraw():
    global balance
    try:
        amount = float(input("kitna paisa nikalna hai : "))
        if amount <= 0:
            print("positive number enter karo!")
            return
        balance -= amount
        print(f"{amount} withdaw ho gaya,New Balance {balance}")
    except ValueError:
        print("Number enter karo, text nahi!")

def check_balance():
    print(f"Aapka Balance: {balance}")

def main():
    """ ye main part yaha se koi bhi ek option use hota hai"""
    while True:
        print("\n" + "="* 30)           #line draw karta hai
        print("      BANK SYSTEM")    # title
        print("="*30)                   #line draw karta hai
        print("1. Paisa deposite Karo")
        print("2. Paise withdraw Karo")
        print("3. Paisa check karo")
        print("4. Exit")

        try :
            choice = input("apni choice bataiye (1-4): ")
            
            if choice =='1':
                deposite()
            elif choice == '2':
                withdraw()
            elif choice == '3':
                check_balance()
            elif choice == 4:
                print("shukriya!, Bank Band ho raha hai!")
            else:
                print("1 se 4 ke bich number enter karo!")

        except ValueError:
            print("Nuber enter karo, Text Nahi!")

if __name__ == "__main__":     #  Yeh check karta hai ki file DIRECTLY run ho rahi hai ya IMPORT ho rahi hai

    main()       # koi specific functions check karne ke liye 