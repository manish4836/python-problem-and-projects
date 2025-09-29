number = [ 3, 4, 25, 78, 98, 43, -9, 60]
#find the second smallest no. of the list

smallest = number[0]
second_smallest =  number[0]

for num in number:
    if num < smallest:
        second_smallest = smallest
        smallest =  num
    elif num > second_smallest and num < smallest:
        second_smallest = num

print(f"the smallest number is {smallest}")
print(f"the second smallest number is {second_smallest}")