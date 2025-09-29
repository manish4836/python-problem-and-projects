squared_dict = {}

for num in range(1, 11):
    squared_dict[num] = num ** 2
print(squared_dict)


# this is another method 
squares = {i: i ** 3 for i in range(1, 15)}
print(squares)
