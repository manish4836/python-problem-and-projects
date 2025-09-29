a = { 2, 4, 5, 7}
b = {3, 6, 8, 9}
 # if check any common element in both sets and print true & false
dis = a.isdisjoint(b)
print(dis)


a = { 2, 4, 5, 7}
b = {3, 6}

print(a.issuperset(b)) # this check the b sets value in a  


a = { 2, 4, 5, 7}
b = {2, 4} # if check the b ke values a me hai ya nahi

print(b.issubset(a))