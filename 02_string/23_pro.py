text = input("enter freq text: ")

freq = {}          # count the frequency of the string


for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch]  = 1

print("character frequencies")    #key = 'h', value = 1
for key, value in freq.items():   # yaha double loop chala   # key = 'e', value = 1
     print(key,":",value)           #key = 'l', value = 2
                                     #key = 'o', value =1
     
