# ----Login Activity Logger----

# This program records the username, date, and time
# of each login in a log file.


from datetime import datetime

username = input("Enter Username: ")

current_time = datetime.now()

with open("activity.log", "a") as file:

    file.write(
        f"{username} logged in at {current_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    )

print("Login Saved Successfully.")
