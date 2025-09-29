set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # {1, 2, 3, 4, 5}  # union
print(set1 & set2)  # {3}  # intersection
print(set1 - set2)  # {1, 2}  # difference
print(set1 ^ set2)  # {1, 2, 4, 5}  # symmetric difference