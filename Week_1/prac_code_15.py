# ----Student Record File Manager----

# This program stores, displays, and searches student
# records using a text file.


FILE_NAME = "students.txt"

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{student_id},{name},{department}\n")

    print("Student added successfully!\n")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nStudent Records")
            print("-" * 40)
            print(file.read())

    except FileNotFoundError:
        print("No records found.\n")


def search_student():
    search_id = input("Enter Student ID to search: ")

    found = False

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                student = line.strip().split(",")

                if student[0] == search_id:
                    print("\nStudent Found")
                    print("ID:", student[0])
                    print("Name:", student[1])
                    print("Department:", student[2])
                    found = True

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("File does not exist.")


while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        break

    else:
        print("Invalid Choice")

