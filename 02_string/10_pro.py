text = input("enter a text: ")

vowels = set("aeiouAEIOU")
count = 0
for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)