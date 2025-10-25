class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        avg = 0
        for values in self.marks:
            avg += values
        print(f"the {self.name} average is {avg / len(self.marks)}")

s1 = student("john", [88, 60, 90])
s1.get_avg()

s1.name = "john doe"
s1.get_avg()

s2 = student("doe", [78, 80, 85])
s2.get_avg()