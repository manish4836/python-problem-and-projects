my_set = set()     #Take input numbers one by one and add them into a set. Print the final set.
n = int(input("How many numbers? "))  # this line is kitne number set me add karna hai

for i in range(n):
    num = int(input("enter the number: ")) # take the numbers 
    my_set.add(num)

print(my_set)