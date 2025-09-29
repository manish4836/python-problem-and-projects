number = (4, 5, 7, 10, 20, 40, 20, 60, 80, 100)

min_value = number[0]
max_value = number[0]

for num in number:
    if num > max_value:
        max_value = num

    elif num < min_value:
        min_value = num

print(min_value)
print(max_value)