

"""
validator.py

This file checks whether the data typed by the user is valid before
we store it. For example: age must be a number, CGPA must be between
0 and 4, and the Student ID must not already be used.

"""


class ValidationError(Exception):
    pass


class Validator:

    @staticmethod
    def validate_not_empty(value, field_name):
        if value is None or str(value).strip() == "":
            raise ValidationError(f"{field_name} cannot be empty.")
        return str(value).strip()

    @staticmethod
    def validate_age(value):
        value = Validator.validate_not_empty(value, "Age")
        if not value.isdigit():
            raise ValidationError("Age must be a valid number (e.g. 20).")
        age = int(value)
        if age < 15 or age > 100:
            raise ValidationError("Age must be between 15 and 100.")
        return age

    @staticmethod
    def validate_cgpa(value):
        value = Validator.validate_not_empty(value, "CGPA")
        try:
            cgpa = float(value)
        except ValueError:
            raise ValidationError("CGPA must be a valid number (e.g. 3.75).")
        if cgpa < 0.0 or cgpa > 4.0:
            raise ValidationError("CGPA must be between 0.0 and 4.0.")
        return round(cgpa, 2)

    @staticmethod
    def validate_semester(value):
        value = Validator.validate_not_empty(value, "Semester")
        if not value.isdigit():
            raise ValidationError("Semester must be a valid number (e.g. 4).")
        semester = int(value)
        if semester < 1 or semester > 12:
            raise ValidationError("Semester must be between 1 and 12.")
        return semester

    @staticmethod
    def validate_unique_id(student_id, existing_ids):
        student_id = Validator.validate_not_empty(student_id, "Student ID")
        if student_id in existing_ids:
            raise ValidationError(f"Student ID '{student_id}' already exists.")
        return student_id