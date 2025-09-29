name = input("enter the name: ")

repeat = {}    # print the first non repeated letter in the name
for ch in name:
    repeat[ch]= repeat.get(ch,0)+1

first_non_repeat = None
for ch in name:
    if repeat[ch]==1:
        first_non_repeat = ch
        break
print("first non repeat letter is", first_non_repeat)
