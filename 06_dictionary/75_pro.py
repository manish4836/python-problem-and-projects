# Check if all values in a dictionary are unique.

marks = {
    'Manish': 72,
    'Amit': 45,
    'Sneha': 88,
    'Ravi': 72,
    'Priya': 45
}

seen = set()
unique = True
for key, value in marks.items():
    if value in seen:
        unique = False
        break
    seen.add(value)

if unique:
    print("All values are unique")
else:
    print("Values are not unique")


# this is the another method

marks = {'Manish': 72, 'Amit': 45, 'Sneha': 88, 'Ravi': 72}

values = list(marks.values())
if len(values) == len(set(values)):
    print("All values are unique")
else:
    print("Values are not unique")