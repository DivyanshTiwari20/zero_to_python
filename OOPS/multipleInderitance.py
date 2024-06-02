'''Question: Create two classes Person and Employee. Employee should inherit from Person and add an attribute employee_id.'''

class Person:
    def __init__(self,name):
        self.name=name  

class Employee(Person):
    def __init__(self,name,employee_id):
        super().__init__(name)
        self.employee_id=employee_id
      


employee = Employee("Ankit", "S69")
print(employee.name)
print(employee.employee_id)