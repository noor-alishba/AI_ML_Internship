# Employee Payroll

# Create:
#  Employee class
# Methods
# bonus()
# annual_salary


class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def annual_salary(self):
        return self.salary*12

    def bonus(self):
        return self.salary*0.1

employee=Employee("Sara",50000)

print(employee.annual_salary())
print(employee.bonus())