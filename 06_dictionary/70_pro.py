data = {"a": 1, "b": None, "c": None, "d": 4}

rep_val = {}    #Write a program to remove all keys with None values from a dictionary.

for key, value in data.items():
    if value is not None:
        rep_val[key] = value

print(rep_val)


# this is another method 

my_dict = {'a': 1, 'b': None, 'c': 9, 'd': None}

cleaned_dict = {key: value for key, value in my_dict.items() if value is not None}
print(cleaned_dict)
