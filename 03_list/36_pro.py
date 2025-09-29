number1 = [2, 5, 8, 9, 16, 17, 25, 50, 52, 60, 63, 2, 5] 
number2= [2, 5, 8, 9, 16, 17, 25, 80, 90, 100, 250]
# print the common element of the list
common = []

for num in number1:
    if num in number2 and num  not in common:
        common.append(num)

print(common)