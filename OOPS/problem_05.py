
class Student:
    def __init__(self, name, age, grade, attendance = 0):
        self.name = name
        self.age = age
        self.attendance = attendance
        self.grade = grade
        print(f"New student created: {self.name} ")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"attendance: {self.attendance}")
        print(f"grade: {self.grade}")

    def mark_present(self,):
        self.attendance += 1
        print(f"{self.name} ki attendance mark ho gayi. total: {self.attendance}")

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name} ka grade update ho gaya: {self.grade}" )
        

student1 = Student("Aarav", 15, "B", 30)
student1.display_info()

student2 = Student("Aaryan", 14, "A", 40)
student2.display_info()

student1.update_grade("A")
student2.update_grade("A+")
student1.display_info()
student2.display_info()

student2.mark_present()
student2.mark_present()
student2.display_info()