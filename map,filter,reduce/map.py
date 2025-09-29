my_list = [1, 2, 3, 4, 5]
list2 = [4, 8, 15, 16]
squared_list1 = list(map(lambda x: x**2, my_list))
squared_list2 = list(map(lambda x: x**2, list2))
print(squared_list1)
print(squared_list2)

# map() ye pure list, tuple ,etc in me sare elements pe apply krta hai


list2 = [4, 8, 15, 16, 5000]
new_list = list(map(lambda x: x**3, list2))
print(new_list)   