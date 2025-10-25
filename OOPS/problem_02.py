class employee:
    
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def get_employee_info(self):
        return f" Employee name: {self.name}, ID: {self.employee_id}, Department: {self.department}"
    

    
employee1 = employee("Alice", "E123", "HR")
print(employee1.get_employee_info())

employee2 = employee("Tonny", "E456", "IT")
print(employee2.get_employee_info())

employee3 = employee("Bob", "E789", "Finance")
print(employee3.get_employee_info())
