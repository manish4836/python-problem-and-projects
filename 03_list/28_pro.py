number = [ 3, 4, 25, 78, 98, 43, -9, 60]


largest = number[0]     # maan lo pehle element hi sabse bada hai 3
second_largest= number[0]   # maan lo dusra bhi bada hai  3

# fir loop me check karo

for num in number:
    if num > largest:
        second_largest = largest   # pehle wala largest ab second ho jayega
        largest = num         # naya number sabse bada ban jayega

    elif num >second_largest and num < largest:
        second_largest = num

print("the largest number is : ",largest)
print("the second largest number is : ", second_largest)



