text = input("enter freq text: ")

freq = {}          # count the frequency of the string


for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch]  = 1

print("character frequencies")
for key, value in freq.items():
    print(key,":",value)


