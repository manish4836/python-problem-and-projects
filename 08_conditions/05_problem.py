num1 = float(input("Enter a number 1: "))
op = input("Enter an operator: ")
num2 = float(input("Enter a number 2: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
elif op == "=":
    print(num1==num2)
else:
    print("Invalid operator")