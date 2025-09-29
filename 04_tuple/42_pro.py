number = (2, 3, 5, 7, 8, 9, 10, 12, 15, 5, 7, 5, 8, 9)

freq = {}
for num in number:    # find the frequency of the each number
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)
for key, value in freq.items():
    print(key, ":" ,value)


    # this is the another method

from collections import Counter

numbers = (2, 3, 5, 7, 8, 9, 10, 12, 15, 5, 7, 5, 8, 9)

freq = Counter(numbers)

print(freq)   # directly prints dictionary-like output
