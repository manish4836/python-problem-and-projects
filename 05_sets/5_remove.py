#remove() or discard()
a = {"manish", "omkar", "lalit", "Aadi"}

a.remove("Aadi") # if other value remove show error
print(a)
a.discard("manish yelne")# and discard is nor show error
print(a)

# a = {"manish", "omkar", "lalit", "Aadi"}
# del a   # delete all set and show error name is not define
# print(a)


a = {"manish", "omkar", "lalit", "Aadi"}
a.clear()
print(a)