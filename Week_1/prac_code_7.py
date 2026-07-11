# Write a program to find highest, lowest and average salarries of three employees


employees = {
    "Ali":50000,
    "Sara":70000,
    "Noor":65000,
    "Ahmed":80000
}

salaries = employees.values()

print("Highest:", max(salaries))
print("Lowest:", min(salaries))
print("Average:", sum(salaries)/len(salaries))