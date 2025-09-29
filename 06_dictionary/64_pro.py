data = {"a": 1, "b": 2, "c": 2, "d": 3}

rep_val = {}

for key, value in data.items():
    if  value != 2:
        rep_val[key] = value
print(rep_val)

#this is another  method

data = {"a": 1, "b": 9, "c": 2, "d": 3}

new_data = {k: v for k, v in data.items() if v != 2}
print(new_data)