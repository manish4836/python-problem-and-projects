number = (4, 5, 7, 10, 20, 40, 20, 60, 80, 100)
#change the type like tuple to list 

num_list = list(number)
      # and then add remove  modify the list
num_list.append(4)
num_list.remove(10)

print(num_list)

#this is another pythonic method 

numbers = (10, 20, 30, 40)

numbers = tuple(x for x in list(numbers)+ [50] if x!= 20)
print(numbers)