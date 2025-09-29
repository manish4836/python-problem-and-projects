num = int(input("enter a number: "))
if num % 5 == 0 and num % 3 == 0 :
    print("the number is divisible by both 3 and 5")
elif num % 5 == 0:
    print("the number is divisible by 5 ")
elif num % 3 == 0:
    print("the number is divisible by 3 ")
else:
    print("the number is not divisible by both 3 and 5")