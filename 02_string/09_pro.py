text = input("enter the text: ")
rev = ""

for ch in text:
    rev = ch + rev  #  prepend each character

print("reverse a string:", rev)