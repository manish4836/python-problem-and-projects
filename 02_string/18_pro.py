text = input("enter the text: ")

count = sum(1 for ch in text if ch.lower()in "aeiou")
print("the vowels is :", count)  #Count vowels in a string