"""
app.py

This file creates the WEB version of the Student Management System
using Flask.

Run this file with:
    python app.py
Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, render_template, request, redirect, url_for, flash

from student_manager import StudentManager
from validator import ValidationError

app = Flask(__name__)
app.secret_key = "student-management-secret-key"  # needed for flash messages to work

# One StudentManager is created when the server starts.
# It stores all students in memory while the app is running.
manager = StudentManager()
manager.load_data()  # automatically load any previously saved data


@app.route("/")
def index():
    """Show the dashboard: statistics cards + a table of all students."""
    students = manager.get_all_students()
    stats = manager.get_statistics()
    return render_template("index.html", students=students, stats=stats)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    """Show the 'Add Student' form, and handle the form when submitted."""
    if request.method == "POST":
        try:
            manager.add_student(
                request.form.get("student_id"),
                request.form.get("name"),
                request.form.get("age"),
                request.form.get("department"),
                request.form.get("semester"),
                request.form.get("cgpa"),
            )
            flash("Student added successfully!", "success")
            return redirect(url_for("index"))
        except ValidationError as error:
            # Show the error to the user and let them try again
            flash(str(error), "error")

    return render_template("add_student.html")


@app.route("/update/<student_id>", methods=["GET", "POST"])
def update_student(student_id):
    """Show the 'Update Student' form for one student, and save changes."""
    student = manager.search_student(student_id)
    if student is None:
        flash(f"No student found with ID '{student_id}'.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        try:
            manager.update_student(student_id, "name", request.form.get("name"))
            manager.update_student(student_id, "age", request.form.get("age"))
            manager.update_student(student_id, "department", request.form.get("department"))
            manager.update_student(student_id, "semester", request.form.get("semester"))
            manager.update_student(student_id, "cgpa", request.form.get("cgpa"))
            flash("Student updated successfully!", "success")
            return redirect(url_for("index"))
        except ValidationError as error:
            flash(str(error), "error")

    return render_template("update_student.html", student=student)


@app.route("/delete/<student_id>", methods=["POST"])
def delete_student(student_id):
    """Delete one student. The confirmation happens in the browser (JavaScript)."""
    deleted = manager.delete_student(student_id)
    if deleted:
        flash("Student deleted successfully!", "success")
    else:
        flash(f"No student found with ID '{student_id}'.", "error")
    return redirect(url_for("index"))


@app.route("/search", methods=["GET", "POST"])
def search_student():
    """Search for a student by their Student ID."""
    student = None
    searched_id = ""

    if request.method == "POST":
        searched_id = request.form.get("student_id", "")
        student = manager.search_student(searched_id)
        if student is None:
            flash(f"No student found with ID '{searched_id}'.", "error")

    return render_template("search.html", student=student, searched_id=searched_id)


@app.route("/sort/<key>")
def sort_students(key):
    """Sort all students by name, department or cgpa."""
    try:
        manager.sort_students(key)
        flash(f"Students sorted by {key}.", "success")
    except ValidationError as error:
        flash(str(error), "error")
    return redirect(url_for("index"))


@app.route("/save")
def save_data():
    """Save all student data to student_data.json."""
    if manager.save_data():
        flash("Data Saved Successfully!", "success")
    else:
        flash("Failed to save data. Check activity.log for details.", "error")
    return redirect(url_for("index"))


@app.route("/load")
def load_data():
    """Load student data from student_data.json."""
    count = manager.load_data()
    flash(f"Data Loaded Successfully! ({count} record(s) loaded)", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)