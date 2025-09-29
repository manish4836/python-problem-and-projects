# Given a dictionary of marks, print the names of students who scored above 50.

marks = {
    'Manish': 72,
    'Amit': 45,
    'Sneha': 88,
    'Ravi': 39,
    'Priya': 51
}

for key, value in marks.items():
    if value > 50:
        print(key)