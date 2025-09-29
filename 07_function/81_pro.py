def max_num(a,b, c):

    if a > b  and a > c:
        print("the maximum number is :", a)
    elif b >c and b > a:
        print("the maximum number is :", b)
    else:
        print("the maximum number is :", c)

x = int(input("enter the number: "))
y = int(input("enter the number: "))
z = int(input("enter the number: "))
max_num(x,y,z)


#this is the another method

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
z = int(input("Enter number 3: "))

print("The maximum number is:", max(x, y, z))

# this is minimum value find method 


x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
z = int(input("Enter number 3: "))

print("The maximum number is:", min(x, y, z))