# ----Employee Salary Report----

# This program reads employee salaries from a file,
# calculates statistics, and saves the report to another file.

input_file = "salary.txt"
output_file = "report.txt"

try:

    with open(input_file, "r") as file:
        salaries = [int(line.strip()) for line in file]

    highest = max(salaries)
    lowest = min(salaries)
    average = sum(salaries) / len(salaries)

    with open(output_file, "w") as report:

        report.write(f"Highest Salary : {highest}\n")
        report.write(f"Lowest Salary : {lowest}\n")
        report.write(f"Average Salary : {average:.2f}\n")

    print("Report Generated Successfully!")

except FileNotFoundError:
    print("Salary file not found.")