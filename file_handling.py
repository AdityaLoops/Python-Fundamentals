"""
File Handling Practice
-----------------------
Covers: safe file reading with `with`, writing lines to a file,
reading/writing CSV with csv.DictReader / DictWriter, appending a new
row, and removing duplicate rows from a CSV based on a unique key.
"""

import csv
import os

# ---------------------------------------------------------------------
# 1. Why `with open(...)` instead of open()/close()
# ---------------------------------------------------------------------
# f = open("notes.txt", "r")
# content = f.read()
# f.close()
#
# Problem: if an error happens between open() and close(), the file
# never gets closed. `with` closes it automatically, even on error.

with open("notes.txt", "w") as f:
    f.write("Line one\n")
    f.write("Line two\n")

with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# ---------------------------------------------------------------------
# 2. Writing a list of words to a file, one per line
# ---------------------------------------------------------------------
words = ["I", "will", "excel", "in", "AI"]

with open("words.txt", "w") as f:
    for word in words:
        f.write(word + "\n")

with open("words.txt", "r") as f:
    print(f.read())

# ---------------------------------------------------------------------
# 3. Reading a CSV with csv.DictReader
# ---------------------------------------------------------------------
# Create a sample CSV so this script is runnable on its own.
sample_rows = [
    {"Employee_ID": "101", "Name": "Aditya Sharma", "Department": "AI", "Salary": "55000", "Join_Date": "2025-06-01"},
    {"Employee_ID": "102", "Name": "Priya Verma", "Department": "AI", "Salary": "58000", "Join_Date": "2025-06-03"},
    {"Employee_ID": "103", "Name": "Rahul Singh", "Department": "Design", "Salary": "52000", "Join_Date": "2025-07-11"},
    {"Employee_ID": "101", "Name": "Aditya Sharma", "Department": "AI", "Salary": "55000", "Join_Date": "2025-06-01"},  # duplicate row
]
fieldnames = ["Employee_ID", "Name", "Department", "Salary", "Join_Date"]

with open("employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sample_rows)

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    print(f"{'Name':<18} | {'Department':<12} | {'Salary':<8}")
    print("-" * 45)
    for row in reader:
        salary = int(row["Salary"])
        print(f"{row['Name']:<18} | {row['Department']:<12} | ${salary:,}")

# ---------------------------------------------------------------------
# 4. Appending a new row to the CSV
# ---------------------------------------------------------------------
new_employee = {
    "Employee_ID": "104",
    "Name": "Gabriel Ross",
    "Department": "Design",
    "Salary": "67000",
    "Join_Date": "2026-03-01",
}

with open("employees.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow(new_employee)
print("\nAdded a new employee row.")

# ---------------------------------------------------------------------
# 5. Removing duplicate rows (by Employee_ID) and rewriting the file
# ---------------------------------------------------------------------
unique_rows = []
seen_ids = set()

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Employee_ID"] not in seen_ids:
            unique_rows.append(row)
            seen_ids.add(row["Employee_ID"])

with open("employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(unique_rows)

print("\nFinal de-duplicated file:")
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Clean up files created by this demo
os.remove("notes.txt")
os.remove("words.txt")
os.remove("employees.csv")
