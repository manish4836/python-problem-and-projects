dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}


if dict2 == dict1:
    print("the both dictionary are equal")
else :
    print("both dictionary are not equal")


# this is another method 

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 7, "a": 5}

is_equal= True
if len(dict1) != len(dict2):
    is_equal = False
else:
    for key, value in dict1.items():
        if key not in dict1 or dict2[key] != value:
            is_equal = False

if is_equal:
    print("both dictionary's are equals")
else :
    print("the dictionary's are not equal")