# Student Management Class


class Student:

    def __init__(self,name,age,department,cgpa):
        self.name=name
        self.age=age
        self.department=department
        self.cgpa=cgpa

    def display(self):
        print(self.name,self.age,self.department,self.cgpa)

    def update_cgpa(self,new_cgpa):
        self.cgpa=new_cgpa

student=Student("Noor",20,"AI",3.7)

student.display()

student.update_cgpa(3.9)

student.display()