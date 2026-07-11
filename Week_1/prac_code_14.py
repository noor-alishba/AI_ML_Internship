# Course Registration System

# Requirements:
# Create
# Student
# Course
# A student can register in multiple courses.


class Course:

    def __init__(self,name):
        self.name=name

class Student:

    def __init__(self,name):
        self.name=name
        self.courses=[]

    def register(self,course):
        self.courses.append(course)

    def display(self):
        print(self.name)
        for course in self.courses:
            print(course.name)

python=Course("Python")
ai=Course("Artificial Intelligence")

student=Student("Noor")

student.register(python)
student.register(ai)

student.display()