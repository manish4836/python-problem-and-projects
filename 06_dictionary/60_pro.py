scores = {"A": 45, "B": 80, "C": 67}
max_val = -1
max_key = ""
for key in scores:
    if scores[key] > max_val:
        max_val = scores[key]
        max_key = key

print(max_key)

# this is another problem

scores = {"A": 45, "B": 80, "C": 67}

max_key = max(scores, key=scores.get)

print("Key with maximum value:", max_key)
