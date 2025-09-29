a = {2, 3, 4, 5, 6, 20, 40, 60, 100}

max_value = None
min_value = None

for num in a:
   if max_value is None or num > max_value:
      max_value = num
   if min_value is None or num < min_value:
      min_value = num

print(max_value)
print(min_value)