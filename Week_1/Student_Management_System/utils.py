
"""
utils.py
--------
This file has small helper functions used by the command-line app
(main.py), such as clearing the screen, printing colored messages,
and showing student data as a neat table.
We use the "colorama" library so the colors work correctly on
Windows, Mac and Linux.
"""

import os
from datetime import datetime

from colorama import Fore, Style, init

# autoreset=True means the color resets automatically after each print,
# so we don't have to add Style.RESET_ALL everywhere.
init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(Fore.CYAN + "\nPress Enter to Continue...")


def print_success(message):
    print(Fore.GREEN + "[SUCCESS] " + message)


def print_warning(message):
    print(Fore.YELLOW + "[WARNING] " + message)


def print_error(message):
    print(Fore.RED + "[ERROR] " + message)


def print_heading(text):
    print(Fore.CYAN + Style.BRIGHT + "\n" + text)
    print(Fore.CYAN + "-" * len(text))


def print_divider():
    print(Fore.BLUE + "=" * 60)


def get_current_datetime():
    return datetime.now().strftime("%d %B %Y, %I:%M %p")


def show_welcome_screen():
    clear_screen()
    print_divider()
    print(Fore.CYAN + Style.BRIGHT + "STUDENT MANAGEMENT SYSTEM".center(60))
    print_divider()
    print(Fore.YELLOW + "Developed using Python (OOP)".center(60))
    print(Fore.YELLOW + get_current_datetime().center(60))
    print_divider()
    input(Fore.GREEN + "\nPress Enter to Continue...")


def print_table(students):
    if not students:
        print_warning("No student records to display.")
        return

    headers = ["ID", "Name", "Age", "Department", "Semester", "CGPA"]
    widths = [10, 20, 6, 15, 10, 6]

    header_row = "".join(h.ljust(w) for h, w in zip(headers, widths))
    print(Fore.CYAN + Style.BRIGHT + header_row)
    print(Fore.CYAN + "-" * sum(widths))

    for student in students:
        row = [
            str(student.student_id),
            str(student.name),
            str(student.age),
            str(student.department),
            str(student.semester),
            str(student.cgpa),
        ]
        print("".join(cell.ljust(w) for cell, w in zip(row, widths)))

    print(Fore.CYAN + "-" * sum(widths))