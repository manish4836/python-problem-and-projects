
#this is intersection
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 3, 6, 8, 10}
s =set1.intersection(set2) # - Returns a new set with common elements.

print(s)
set1.intersection_update(set2)   #- Modifies set1 in place to keep only common elements

print(set1)
