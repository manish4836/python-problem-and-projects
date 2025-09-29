key = [ "no.", "percent", "name", "college name", "year"]
values = [ 13 , 98, "manish" , "raisoni", 2]

dict = {}       # print the keys and values in dictionary

for i in range(len(key)):
    dict[key[i]] = values[i]

print(dict)

#this is another way

# keys = ["name", "age", "city"]
# values = ["Manish", 21, "Nagpur"]

# my_dict = dict(zip(keys, values))
# print(my_dict)