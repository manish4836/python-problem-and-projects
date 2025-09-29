number = [2, 5, 8, 9, 16, 17, 25, 50, 52, 60, 63, 2, 5] 
   #remove duplicates from the list
duplicate = []
for num in number:
    if num not in duplicate:
        duplicate.append(num)

print(duplicate)