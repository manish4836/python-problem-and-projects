list_a = [1, 2, 3, 4] 
list_b = [3, 4, 5, 6]


print(set(list_a).intersection(list_b))  # list_a ke elements jo list_b me hai

print(set(list_a).union(list_b))  # list_a ke elements jo list_b me hai and list_b ke elements jo list_a me hai

print(set(list_a).difference(list_b))   # list_a ke elements jo list_b me nahi hai

print(set(list_b).difference(list_a))   # list_b ke elements jo list_a me nahi hai

print(set(list_a).symmetric_difference(list_b))   # list_a ke elements jo list_b me nahi hai and list_b ke elements jo list_a me nahi hai

print(set(list_a).issubset(list_b))   # list_a ke elements jo list_b me hai all hai to true

print(set(list_a).issuperset(list_b))   # list_b ke elements jo list_a me hai all hai to true

print(set(list_a).isdisjoint(list_b))   # list_a ke elements jo list_b me nahi hai and list_b ke elements jo list_a me nahi hai all hai to true

print(set(list_a).copy())   # list_a ke elements ko copy karega

print(set(list_a).update(list_b))   # list_a ke elements ko update karega list_b ke elements se