friends = ["Apple", "orange", 5, 345.06, False, "Aaakash", "Rohan"]
list_2 = ["manish","harry",35,]
print(friends)   #unlike Strings lists are mutable in lists
list_2.clear()
print(list_2)

friends.append("manish") # add the single value at the end
friends.insert(5,8)
print(friends)

friends.extend([46,25])    #Adds multiple items (from another list, tuple, string, etc.)
print(friends)
friends.pop(3)   #removes the last item or the item at the given index
print(friends)

friends.remove("Aaakash")
print(friends)


a= [1,2,3,4,5]
a.insert(2, 4)
print(a)
print(a.index(5)) #index value print karne ke liye
print(a.count(4)) #count the values
a.reverse() #reverse the list
print(a)

list = [9,7,0,34,65,100]
list.sort()
print(list)
list2 = list.copy() # create a copy of the list
print(list2)