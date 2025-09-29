'''text = input("enter the text: ")
                          #Write a program to count the number of consonants in a string.
count = 0

consonats= ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

for ch in text:
    if ch in consonats:
        count += 1

print("the no of consonants is :", count)'''


'''
text = input("enter the text: ")    #  this is another method

count= 0
vowels = "aeiouAEIOU"

for ch in text:
    if ch.isalpha() and ch not in vowels:
        count += 1

print("The no.of consonants is :", count)'''




name = input("enter the text: ")

count = sum(1 for ch in name if ch.isalpha() and ch.lower()  not in "aeiou")
print("the number of consonants is : ", count)