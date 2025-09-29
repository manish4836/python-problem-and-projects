str1 = input("enter the name: ")
str2 = input("enter the nume: ")

if sorted(str1) == sorted(str2):
    print("anagram")
else:
    print("not anagram")