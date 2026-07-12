#   🎓 Student Management System

A Python-based Student Management System with both a **command-line interface** and a **Flask web interface**. Both interfaces share a single core module, so records added, updated, or deleted from one are immediately reflected in the other, and data persists between sessions in a local JSON file.

##  ✨ Features

- **Add Student** – create a new record with a unique Student ID
- **View All Students** – list every record in a formatted table
- **Search Student** – look up a record by Student ID
- **Update Student** – edit name, age, department, semester, or CGPA
- **Delete Student** – remove a record with confirmation
- **Sort Students** – order records by name, department, or CGPA
- **Statistics** – total students, highest/lowest/average CGPA, and per-department counts
- **Save / Load Data** – persist records to `student_data.json`
- **Activity Logging** – every action is timestamped in `activity.log`
- **Input Validation** – ID uniqueness, age (15–100), semester (1–12), and CGPA (0.0–4.0) are validated before saving
- **Dual Interface** – identical functionality via terminal or browser

##  🛠️ Technologies Used

- Python 3
- Flask (web interface)
- Colorama (colored CLI output)
- JSON (data storage)
- Jinja2 / HTML (web templates)

##  🗂️ Project Structure

```
student-management-system/
├── main.py             # Command-line application entry point
├── app.py               # Flask web application entry point
├── student_manager.py   # Core business logic (add, search, update, delete, sort, stats)
├── student.py            # Student class (data model)
├── validator.py          # Input validation rules and ValidationError
├── file_manager.py       # JSON file read/write operations
├── logger.py              # Activity logging to activity.log
├── utils.py                # CLI helpers (colored output, tables, menus)
├── templates/               # HTML templates used by the Flask app
├── student_data.json         # Generated data file (created at runtime)
└── activity.log                # Generated log file (created at runtime)
```

##  🚀 How to Run the Project

### Prerequisites
```bash
pip install flask colorama
```

### Command-Line Version
```bash
python main.py
```

### Web Version
```bash
python app.py
```
Then open **http://127.0.0.1:5000** in your browser.

```
```
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

```
```

## 🧑‍🎓 Student Fields

| Field       | Type   | Validation Rule                       |
|-------------|--------|----------------------------------------|
| Student ID  | str    | Required, must be unique                |
| Name        | str    | Required, non-empty                     |
| Age         | int    | Numeric, between 15 and 100             |
| Department  | str    | Required, non-empty                     |
| Semester    | int    | Numeric, between 1 and 12               |
| CGPA        | float  | Numeric, between 0.0 and 4.0            |

```
```
## 🏗️ OOP Design Highlights

- **Encapsulation** — `Student` fields are private and accessed via
  properties; `StudentManager` hides the internal student list.
- **Abstraction** — High-level methods (`add_student`, `sort_students`,
  `get_statistics`) hide implementation details from `main.py`.
- **Single Responsibility** — Each module has one clear job:
  validation, persistence, logging, or UI.
- **Polymorphism** — `Student.__str__` overrides the default string
  representation for clean, class-specific display.

```
```

## 📝 Logging

- Every significant action (add, update, delete, save, load, errors) is
recorded in `activity.log` with a timestamp, e.g.:

```
2026-07-10 14:32:10 | INFO | Added student: S001 - Ayesha Khan
2026-07-10 14:33:02 | INFO | Saved 5 student record(s) to student_data.json.

```
```
```
##  🔮 Future Improvements

- Migrate storage from JSON to a relational database
- Add authentication for the web interface
- Add CSV/Excel export for reports and statistics
```
```
```
```
##  👩‍💻 Author

- Developed by **Noor Alishba Sajid** as part of an internship project.

## 📄 License

- This project is open-source and free to use for learning and
portfolio purposes. 