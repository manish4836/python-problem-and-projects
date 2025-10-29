class employee:
    
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def get_employee_info(self):
        return f" Name: {self.name}, ID: {self.employee_id}, Department: {self.department}"
    
class manager(employee):
    
    def __init__(self, name, employee_id, department, team_size):
        super().__init__(name, employee_id, department)
        self.team_size = team_size

    def get_employee_info(self):
        basec_info = super().get_employee_info()
        return f"{basec_info}, Team Size: {self.team_size}"
    

manager1 = manager("Om yelne", "M123", "Sales", 15)
print(manager1.get_employee_info())

manager2 = manager("manish yelne", "M567", "Sales", 25)
print(manager2.get_employee_info())

 