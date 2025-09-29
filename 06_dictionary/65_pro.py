data = {"a": 1, "b": 7, "c": 3, "d": 4}
sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
print(sorted_items)

# sorted ka use kar ke har key-value pair ko tuple mein convert kar diya hai aur unhe value ke hisaab se sort kar diya hai.

#x[1] ka matlab hai us tuple ka second element (index 1 wala). Jaise, ('a', 1) mein x[1] ki value 1 hai.


data = {"a": 1, "b": 8, "c": 3, "d": 4}

# sort by values (descending)
sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)

# convert back to dictionary
sorted_dict = dict(sorted_items)

print(sorted_dict)

