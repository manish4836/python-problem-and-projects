multiply = lambda x, y : x * y 

print(multiply(5, 4))


#this is another problem

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = filter(lambda num : num % 2 == 0, numbers)

even_number_list = list(my_list)
print(even_number_list)