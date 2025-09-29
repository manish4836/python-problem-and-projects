word = "mississippi"

letter_count ={}

for ch in word:
    letter_count[ch] = letter_count.get(ch, 0)+ 1

print(letter_count)