class Student:
    def  __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        print(f"Create A Student {self.name} ")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

student1 = Student('manish yelne', 20, 'A')
student2 = Student('om yelne', 15, 'A+')

print(student1.display_info())
print(student2.display_info())