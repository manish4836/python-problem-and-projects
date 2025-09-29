name = input("enter the text: ")
# the input is unique hai ya nahi
result = ""

for ch in name:
    if ch not in result:
        result += ch

print ("the unique character is: ",result)

#this is another method 

name = input("Enter the text: ")

if len(set(name)) == len(name):
    print("All characters are unique ✅")
else:
    print("Not unique ❌")



#this is another mathod for logic



name = input("Enter the text: ")

unique = True
for ch in name:
    if name.count(ch) > 1:   # check agar char 1 se zyada baar aaya
        unique = False
        break

if unique:
    print("All characters are unique ✅")
else:
    print("Not unique ❌")
