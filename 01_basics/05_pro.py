"""num = int(input("enter a number: "))    #some of 3 digits

d1 = num % 10   # last digit
num = num // 10  # remove last digit
d2 = num % 10 # new last digit
num = num // 10 # remove new last digit

d3 = num   # remaining digit
sum = d1 + d2 + d3
print("the sum of the digits is: ", sum)"""



num = int(input("enter a number: "))   # this is another method sum of multiple digits

print(sum(int(digit) for digit in str(num))) 




 # str(num) → number ko string banaya (e.g., 1234 → "1234")

# for digit in str(num) → har digit loop me aayegi ('1', '2', '3', '4')

# int(digit) → har digit ko integer me convert kiya

# sum(...) → sabko add kar diya