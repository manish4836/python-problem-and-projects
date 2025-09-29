
# symmetric difference

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8, 10}
s = set1.difference(set2) # print uncommon values
print(s)
set1.symmetric_difference_update(set2) # aisi value print karta hai jo ek dushre ke pass nhi hai
print(set1)