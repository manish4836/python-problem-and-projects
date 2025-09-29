number = [2, 5, 8, 9, 16, 17, 25, 50, 52, 60, 63, 2, 5] 

freq = {}
for num in number: # count the each element how much time
    if num in freq :
        freq[num] += 1
    else:
        freq[num] = 1
    print 

for key, value in freq.items():
 print(key ,":", value)