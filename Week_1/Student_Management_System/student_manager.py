

"""
student_manager.py
This file contains the StudentManager class - the "brain" of the
project. It keeps the list of all students in memory and gives us
simple functions to add, search, update, delete, sort students, and
calculate statistics.
"""

from student import Student, student_from_dict
from validator import Validator, ValidationError
from file_manager import FileManager
from logger import log_action


class StudentManager:

    def __init__(self):
        """Start with an empty list of students."""
        self.students = []
        self.file_manager = FileManager()

    # Add / Search / Update / Delete

    def add_student(self, student_id, name, age, department, semester, cgpa):
        """Validate the input and add a new student to the list."""
        existing_ids = [s.student_id for s in self.students]

        student_id = Validator.validate_unique_id(student_id, existing_ids)
        name = Validator.validate_not_empty(name, "Name")
        age = Validator.validate_age(age)
        department = Validator.validate_not_empty(department, "Department")
        semester = Validator.validate_semester(semester)
        cgpa = Validator.validate_cgpa(cgpa)

        new_student = Student(student_id, name, age, department, semester, cgpa)
        self.students.append(new_student)
        log_action(f"Added student: {student_id} - {name}")
        return new_student

    def get_all_students(self):
        return self.students

    def search_student(self, student_id):
        student_id = student_id.strip()
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update_student(self, student_id, field, new_value):
        student = self.search_student(student_id)
        if student is None:
            raise ValidationError(f"No student found with ID '{student_id}'.")

        field = field.lower().strip()

        if field == "name":
            student.name = Validator.validate_not_empty(new_value, "Name")
        elif field == "age":
            student.age = Validator.validate_age(new_value)
        elif field == "department":
            student.department = Validator.validate_not_empty(new_value, "Department")
        elif field == "semester":
            student.semester = Validator.validate_semester(new_value)
        elif field == "cgpa":
            student.cgpa = Validator.validate_cgpa(new_value)
        else:
            raise ValidationError(f"'{field}' is not a valid field to update.")

        log_action(f"Updated student {student_id}: {field} -> {new_value}")
        return student

    def delete_student(self, student_id):
        """Remove a student from the list by ID. Returns True/False."""
        student = self.search_student(student_id)
        if student is None:
            return False
        self.students.remove(student)
        log_action(f"Deleted student: {student_id}")
        return True

    # Sorting

    def sort_students(self, key="name"):
        key = key.lower().strip()
        if key == "name":
            self.students.sort(key=lambda s: s.name.lower())
        elif key == "department":
            self.students.sort(key=lambda s: s.department.lower())
        elif key == "cgpa":
            self.students.sort(key=lambda s: s.cgpa, reverse=True)
        else:
            raise ValidationError(f"'{key}' is not a valid sort option.")

        log_action(f"Sorted students by {key}.")
        return self.students

    # Statistics

    def get_statistics(self):
        
        if not self.students:
            return None

        cgpas = [s.cgpa for s in self.students]

        department_counts = {}
        for student in self.students:
            department_counts[student.department] = (
                department_counts.get(student.department, 0) + 1
            )

        stats = {
            "total_students": len(self.students),
            "highest_cgpa": max(cgpas),
            "lowest_cgpa": min(cgpas),
            "average_cgpa": round(sum(cgpas) / len(cgpas), 2),
            "department_counts": department_counts,
        }
        log_action("Generated statistics report.")
        return stats

    # File Handling 

    def save_data(self):
        """Save all students to the JSON file. Returns True/False."""
        return self.file_manager.save_data(self.students)

    def load_data(self):
        """Load students from the JSON file into memory. Returns count loaded."""
        raw_data = self.file_manager.load_data()
        self.students = [student_from_dict(item) for item in raw_data]
        return len(self.students)