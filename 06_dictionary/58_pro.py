data = {"a": 5, "b": 15, "c": "hello"}

for key  in  data:
    if isinstance(data[key], int):
        data[key]= data[key] + 10

print(data)

#this is another method 

student = {"math": 40, "science": 50, "name": "Manish"}
for key in student:
    if isinstance(student[key],int):
        student[key] = student[key] + 10

print(student)

# this is another method 

student = {"math": 40, "science": 50, "name": "Manish"}

student = {k: (v + 10 if isinstance(v, int) else v) for k, v in student.items()}

print(student)
