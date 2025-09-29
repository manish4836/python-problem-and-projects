text = input("enter the text: ")

result = ""
for ch in text:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch)-32)
    else:
        result += ch

print("uppercase text",result)