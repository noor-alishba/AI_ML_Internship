

"""
main.py
This is the entry point for the COMMAND-LINE version of the Student
Management System. It shows a text menu, asks the user for input,
and calls the StudentManager to do the actual work.

Run this file with:
    python main.py
"""

from colorama import Fore

from student_manager import StudentManager
from validator import ValidationError
from logger import log_action, log_error
from utils import (
    clear_screen,
    pause,
    print_success,
    print_warning,
    print_error,
    print_heading,
    print_divider,
    print_table,
    show_welcome_screen,
)


class App:

    def __init__(self):
        self.manager = StudentManager()
        self.menu_options = {
            "1": self.add_student,
            "2": self.view_all_students,
            "3": self.search_student,
            "4": self.update_student,
            "5": self.delete_student,
            "6": self.sort_students,
            "7": self.show_statistics,
            "8": self.save_data,
            "9": self.load_data,
            "10": self.exit_app,
        }
        self.running = True

    def run(self):
        show_welcome_screen()
        self.load_data(silent=True)  # auto-load data when the program starts

        while self.running:
            self.show_main_menu()
            choice = input(Fore.GREEN + "\nEnter your choice (1-10): ").strip()

            action = self.menu_options.get(choice)
            if action is None:
                print_error("Invalid choice. Please select a number between 1 and 10.")
                pause()
                continue

            try:
                action()
            except ValidationError as error:
                print_error(str(error))
                log_error(f"Validation error: {error}")
                pause()
            except Exception as error:
                print_error(f"Something went wrong: {error}")
                log_error(f"Unexpected error: {error}")
                pause()

    def show_main_menu(self):
        """Print the main menu options."""
        clear_screen()
        print_divider()
        print(Fore.CYAN + "STUDENT MANAGEMENT SYSTEM - MAIN MENU".center(60))
        print_divider()
        print("  1. Add Student")
        print("  2. View All Students")
        print("  3. Search Student")
        print("  4. Update Student")
        print("  5. Delete Student")
        print("  6. Sort Students")
        print("  7. Show Statistics")
        print("  8. Save Data")
        print("  9. Load Data")
        print("  10. Exit")
        print_divider()

    # Menu actions

    def add_student(self):
        clear_screen()
        print_heading("Add New Student")

        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        department = input("Enter Department: ")
        semester = input("Enter Semester: ")
        cgpa = input("Enter CGPA (0.0 - 4.0): ")

        student = self.manager.add_student(student_id, name, age, department, semester, cgpa)
        print_success(f"Student '{student.name}' added successfully!")
        pause()

    def view_all_students(self):
        clear_screen()
        print_heading("All Students")
        print_table(self.manager.get_all_students())
        pause()

    def search_student(self):
        clear_screen()
        print_heading("Search Student")
        student_id = input("Enter Student ID to search: ")
        student = self.manager.search_student(student_id)

        if student:
            print_success("Student found:")
            print_table([student])
        else:
            print_warning(f"No student found with ID '{student_id}'.")
        pause()

    def update_student(self):
        clear_screen()
        print_heading("Update Student")
        student_id = input("Enter Student ID to update: ")

        student = self.manager.search_student(student_id)
        if not student:
            print_warning(f"No student found with ID '{student_id}'.")
            pause()
            return

        print_success("Student found:")
        print_table([student])

        print("\nWhich field would you like to update?")
        print("  1. Name\n  2. Age\n  3. Department\n  4. Semester\n  5. CGPA")
        choice = input("Enter choice (1-5): ").strip()

        field_map = {"1": "name", "2": "age", "3": "department", "4": "semester", "5": "cgpa"}
        field = field_map.get(choice)

        if not field:
            print_error("Invalid field choice.")
            pause()
            return

        new_value = input(f"Enter new value for {field}: ")
        updated_student = self.manager.update_student(student_id, field, new_value)
        print_success("Student updated successfully!")
        print_table([updated_student])
        pause()

    def delete_student(self):
        clear_screen()
        print_heading("Delete Student")
        student_id = input("Enter Student ID to delete: ")

        student = self.manager.search_student(student_id)
        if not student:
            print_warning(f"No student found with ID '{student_id}'.")
            pause()
            return

        print_table([student])
        confirm = input(Fore.YELLOW + "Are you sure you want to delete this student? (yes/no): ").strip().lower()

        if confirm == "yes":
            self.manager.delete_student(student_id)
            print_success("Student deleted successfully!")
        else:
            print_warning("Deletion cancelled.")
        pause()

    def sort_students(self):
        clear_screen()
        print_heading("Sort Students")
        print("Sort by:\n  1. Name\n  2. Department\n  3. CGPA")
        choice = input("Enter choice (1-3): ").strip()

        key_map = {"1": "name", "2": "department", "3": "cgpa"}
        key = key_map.get(choice)

        if not key:
            print_error("Invalid sort option.")
            pause()
            return

        sorted_students = self.manager.sort_students(key)
        print_success(f"Students sorted by {key}.")
        print_table(sorted_students)
        pause()

    def show_statistics(self):
        clear_screen()
        print_heading("Student Statistics")
        stats = self.manager.get_statistics()

        if stats is None:
            print_warning("No student data available to generate statistics.")
            pause()
            return

        print(f"Total Students   : {stats['total_students']}")
        print(f"Highest CGPA     : {stats['highest_cgpa']}")
        print(f"Lowest CGPA      : {stats['lowest_cgpa']}")
        print(f"Average CGPA     : {stats['average_cgpa']}")

        print(Fore.CYAN + "\nDepartment-wise Student Count:")
        for department, count in stats["department_counts"].items():
            print(f"  {department}: {count}")

        pause()

    def save_data(self):
        clear_screen()
        print_heading("Save Data")
        if self.manager.save_data():
            print_success("Data Saved Successfully!")
        else:
            print_error("Failed to save data. Check activity.log for details.")
        pause()

    def load_data(self, silent=False):
        if not silent:
            clear_screen()
            print_heading("Load Data")

        count = self.manager.load_data()
        if count > 0:
            print_success(f"Data Loaded Successfully! ({count} record(s) loaded)")
        else:
            print_warning("No existing data found. Starting fresh.")

        if not silent:
            pause()

    def exit_app(self):
        clear_screen()
        print_heading("Exiting Student Management System")
        self.manager.save_data()
        print_success("Data Saved Successfully!")
        print(Fore.CYAN + "\nThank you for using the Student Management System. Goodbye!\n")
        log_action("Application exited.")
        self.running = False


def main():
    app = App()
    try:
        app.run()
    except KeyboardInterrupt:
        print_warning("\nInterrupted by user. Saving data before exit...")
        app.manager.save_data()
        print_success("Data Saved Successfully! Goodbye!")
        log_action("Application interrupted by user (KeyboardInterrupt).")

if __name__ == "__main__":
    main()