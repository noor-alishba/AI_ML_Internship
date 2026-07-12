

"""
logger.py

This file saves a small note in "activity.log" every time something
important happens, like adding, updating, or deleting a student.
Each note includes the date and time it happened.
"""

from datetime import datetime

LOG_FILE = "activity.log"


def write_log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp} | {level} | {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_line)


def log_action(message):
    write_log("INFO", message)


def log_error(message):
    """Log an error message, e.g. 'Failed to save data'."""
    write_log("ERROR", message)