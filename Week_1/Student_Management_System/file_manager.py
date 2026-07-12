"""
file_manager.py

This file is responsible for saving and loading student data using a
JSON file called "student_data.json".
"""

import json
import os

from logger import log_action, log_error

DATA_FILE = "student_data.json"


class FileManager:

    def __init__(self, file_path=DATA_FILE):
        self.file_path = file_path

    def save_data(self, students):
        
        try:
            data = [student.to_dict() for student in students]
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            log_action(f"Saved {len(students)} student record(s) to {self.file_path}.")
            return True
        except (IOError, OSError) as error:
            log_error(f"Failed to save data: {error}")
            return False

    def load_data(self):
       
        if not os.path.exists(self.file_path):
            log_action("No existing data file found. Starting with an empty list.")
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if content == "":
                    return []
                data = json.loads(content)
            log_action(f"Loaded {len(data)} student record(s) from {self.file_path}.")
            return data
        except (IOError, OSError, json.JSONDecodeError) as error:
            log_error(f"Failed to load data: {error}")
            return []