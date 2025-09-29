name = input("enter a name: ")

result = ""

for ch in name:           #Remove all duplicates from a string
    if ch not in result:
        result += ch

print(result)