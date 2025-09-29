a = input("enter a name ")

print(f"Good Afternoon {a}")
print("good afternoon ", a)
friends = ["Apple", "orange", 5, 345.06, False, "Aaakash", "Rohan"]

print(friends)

friends.append("manish") # add the single value at the end
print(friends)
friends.extend([46,25])    #Adds multiple items (from another list, tuple, string, etc.)

print(friends)

import pyjokes

joke = pyjokes.get_joke()
print(joke)


a= 12
print(type(a))


a="manish"
b= a[0:4]
print(b)  #start from index 0 to 4   

name = "manish"

print (name[-5:-1])  # start from read to -5 but value of -1 is not read 
print(name[1:5])  # it will be read the 1 but not 5



name = "abcdefghijklmnopqrstuvwxyz"  #  firstly take 1  to 6 charcter i.e b to g

print(name[1:7:3])    # then skip the next two charcter because the value is given 3 
print(len(name))   #take first charcter then skip next two character and then again take  the ans is "be"
