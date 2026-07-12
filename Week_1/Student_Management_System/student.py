

"""
student.py

This file defines the Student class.

"""


class Student:

    def __init__(self, student_id, name, age, department, semester, cgpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department
        self.semester = semester
        self.cgpa = cgpa

    def to_dict(self):
        
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "semester": self.semester,
            "cgpa": self.cgpa,
        }

    def __str__(self):
        return (
            f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | "
            f"Department: {self.department} | Semester: {self.semester} | "
            f"CGPA: {self.cgpa}"
        )


def student_from_dict(data):
    
    return Student(
        student_id=data.get("student_id"),
        name=data.get("name"),
        age=data.get("age"),
        department=data.get("department"),
        semester=data.get("semester"),
        cgpa=data.get("cgpa"),
    )