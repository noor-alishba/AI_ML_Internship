# 🎓 Student Management System

A professional, menu-driven **Student Management System** built with
**Python 3** and **Object-Oriented Programming (OOP)**. Designed as a
clean, modular, beginner-friendly project suitable for an AI/ML
internship submission or GitHub portfolio.

---

## ✨ Features

- **Beautiful CLI welcome screen** with project title and live date/time
- **Full CRUD operations** — Add, View, Search, Update, Delete students
- **Sorting** by Name, Department, or CGPA
- **Statistics dashboard** — total students, highest/lowest/average CGPA,
  department-wise counts
- **JSON-based persistence** — auto-loads on startup, auto-saves on exit
- **Input validation** with friendly error messages (empty fields,
  numeric checks, CGPA range, unique student IDs)
- **Colorized output** using `colorama` (green = success, yellow =
  warning, red = error, cyan = headings)
- **Activity logging** — every action is timestamped in `activity.log`
- **Robust exception handling** throughout the app

---

## 🗂️ Project Structure

```
Student_Management_System/
│
├── main.py              # Application entry point & CLI menu logic
├── student.py            # Student class (data model)
├── student_manager.py     # Core business logic (CRUD, sort, stats)
├── file_manager.py        # JSON file save/load handling
├── validator.py           # Input validation logic
├── logger.py               # Activity logging setup
├── utils.py                 # CLI helpers (colors, tables, screens)
├── student_data.json         # Saved student records (auto-generated)
├── activity.log                # Action log (auto-generated)
├── requirements.txt             # Python dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Student_Management_System.git
   cd Student_Management_System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

Requires **Python 3.8+**.

---

## 🧭 Main Menu

```
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Sort Students
7. Show Statistics
8. Save Data
9. Load Data
10. Exit
```

---

## 🧑‍🎓 Student Fields

| Field       | Type   | Validation Rule                       |
|-------------|--------|----------------------------------------|
| Student ID  | str    | Required, must be unique                |
| Name        | str    | Required, non-empty                     |
| Age         | int    | Numeric, between 15 and 100             |
| Department  | str    | Required, non-empty                     |
| Semester    | int    | Numeric, between 1 and 12               |
| CGPA        | float  | Numeric, between 0.0 and 4.0            |

---

## 🏗️ OOP Design Highlights

- **Encapsulation** — `Student` fields are private and accessed via
  properties; `StudentManager` hides the internal student list.
- **Abstraction** — High-level methods (`add_student`, `sort_students`,
  `get_statistics`) hide implementation details from `main.py`.
- **Single Responsibility** — Each module has one clear job:
  validation, persistence, logging, or UI.
- **Polymorphism** — `Student.__str__` overrides the default string
  representation for clean, class-specific display.

---

## 📝 Logging

Every significant action (add, update, delete, save, load, errors) is
recorded in `activity.log` with a timestamp, e.g.:

```
2026-07-10 14:32:10 | INFO | Added student: S001 - Ayesha Khan
2026-07-10 14:33:02 | INFO | Saved 5 student record(s) to student_data.json.
```

---

## 📄 License

This project is open-source and free to use for learning and
portfolio purposes.