number = [2, 5, 8, 9, 16, 17, 25]

rev_list = [] # reverse the list without using reverse()

for i in range(len(number)-1,-1,-1):
    rev_list .append(number[i])
print(rev_list)

#this is the another method

list =[5 , 6, 8, 9, 15,25]
rev = []
for num in list:
    rev.insert(0,num)

print(rev)