number = [2, 5, 8, 9, 16, 17, 25, 50, 52, 60, 63] 

even_num = 0
                # find the sum of the all even number 
for num in number:
    if num %2 == 0:
        even_num += num

print("the sum of the even number is", even_num)

#this is the another method

number = [2, 5, 8, 9, 16, 17, 25, 50, 52, 60, 63] 

even_num = sum(num for num in number if  num %2 ==0)

print("the sum of the even number is", even_num)