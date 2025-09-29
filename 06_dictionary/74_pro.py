# Use a set to find all unique values from a dictionary.
marks = {
    'Manish': 72,
    'Amit': 45,
    'Sneha': 88,
    'Ravi': 72,
    'Priya': 45
}

unique_val = set(marks.values())
print(unique_val)