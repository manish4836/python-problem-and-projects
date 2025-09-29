a = int(input("enter a number a: "))
b = int(input("enter a number b: "))
c = int(input("enter a number c: ")) 

if a > b :
    largest = a
else :
    largest = b
if c > largest :
    largest = c

print("the largest number is: ", largest)

if a == b == c:
    print("all numbers are equal")

else :
    largest = b