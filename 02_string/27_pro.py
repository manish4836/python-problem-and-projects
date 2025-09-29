number = [ 2, 4, 6, 27, 90, 360, -45, -80]

max_num = number[0]
min_num = number[0]

for num in number:
    if num > max_num :
        max_num = num

    elif num < min_num:
        min_num = num

print(f"the maximum number is {max_num}")
print(f"the minimum number is {min_num}")