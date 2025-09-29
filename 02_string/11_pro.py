text =input("enter a text: ")

rev = ""
for ch in text:
    rev = ch + rev
print(rev)

if text == rev:
    print("polidrome")
else:
    print("not polidrome")