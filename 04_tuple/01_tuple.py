a = (5,36,52,258,2252,"manish", "yelne",52)

print(type(a))
print(a)

print(a.count(52)) # this is count the particular value how many times it appears

print(a.index(2252))   # this is find the index of the particular value then not read another 2252

repeated = a * 9  # repeat the tuple 9 times
print(repeated)


print(36 in a)  # it will return true if the value is present in the tuple otherwise false

print(len(a))  # it will return the length of the tuple


# ...existing code...
int_values = [x for x in a if isinstance(x, int)]
print(min(int_values))  # minimum integer value
print(max(int_values))  # maximum integer value
# ...existing code...

tuple=(7,3,7,8,)   #the value is 7378
a, b, c, d = tuple 

print(a, b, c, d)

