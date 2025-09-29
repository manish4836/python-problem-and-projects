original = {'a': 5, 'b': 3, 'c': 2}
reversed_dict = {}

for key, value in original.items():
    reversed_dict[value] = key

print(reversed_dict)


original = {'a': 6, 'b': 28, 'c': 4}

reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)
