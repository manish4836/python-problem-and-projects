# Create a dictionary where each key is a number 1–5, and each value is a set containing the multiples of that number up to 20.

multiples_dict = {}

for i in range(1, 6):
    multiples = set()
    for j in range(1 , 21):
        if j % i == 0:
            multiples.add(j)
    multiples_dict[i] = multiples
print(multiples_dict)


# this is another method

multiples_dict = {}

for n in range(1, 6):   # keys from 1 to 5
    multiples_dict[n] = set(range(n, 21, n))   # multiples up to 20

print(multiples_dict)
