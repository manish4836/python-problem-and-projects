number1 = [2, 5, 8, 9, 16, 17, 25, 50, 52, 60, 63, 2, 5] 
number2= [2, 5, 8, 9, 16, 17, 25, 80, 90, 100, 250]

#merged two list without duplicate 
merged = []
for num in number1 + number2:

    if num not in merged:
        merged.append(num)
print(merged)


#this is the another method 
number1 = [2, 5, 8, 9, 16, 17, 25, 50, 52, 60, 63, 2, 5] 
number2= [2, 5, 8, 9, 16, 17, 25, 80, 90, 100, 250]

merged = list(set(number1 + number2))
print(sorted(merged))