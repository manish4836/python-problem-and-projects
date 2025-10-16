my_list = [1, 4, 8, 9, 12, 15, 20]
largest = my_list[0]
second_largest = my_list[0]
for num in my_list:
    if num > second_largest:
        largest = second_largest
        second_largest = num

    elif num > second_largest and num < largest:
        second_largest = num

print(f"The largest number is {largest}")
print(f"The second largest number is {second_largest}")