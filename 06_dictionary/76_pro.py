# Write a program to swap keys and values in a dictionary safely (avoid overwriting duplicates).

original = {
    'A': 67,
    'B': 23,
    'C': 45,
    'D': 56,
    'E': 12,
    'F': 69,
    'G': 67,
    'H': 23
}

rev_dict = {}
for key, value in original.items():
    rev_dict[value] = key

print(rev_dict)

# this is another method

original = {
    'A': 90,
    'B': 23,
    'C': 45,
    'D': 56,
    'E': 80,
    'F': 69,
    'G': 67,
    'H': 23
}

swapped = {}

for key, value in original.items():
    if value in swapped:
        swapped[value].append(key)
    else:
        swapped[value] = [key]

print(swapped)