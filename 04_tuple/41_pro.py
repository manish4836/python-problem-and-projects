number = (2, 3, 5, 7, 8, 9, 10, 12, 15)
 # find the index of an elment
target = 8
pos = 0
for num in number:
    if num == 8 :
        print (f"the index of,{target} is {pos}")
        break
    pos +=1

# this is the another method

number = (2, 3, 5, 7, 8, 9, 10, 12, 15)

target = 9

for index, value in enumerate(number):
    print(f"the indesx of {target} is {value}")
    break