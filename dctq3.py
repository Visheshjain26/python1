employees = [
    {"dept_no": 101, "roll_no": 1, "salary": 50000},
    {"dept_no": 102, "roll_no": 2, "salary": 60000},
    {"dept_no": 101, "roll_no": 3, "salary": 45000},
    {"dept_no": 102, "roll_no": 4, "salary": 75000},
    {"dept_no": 103, "roll_no": 5, "salary": 55000}
]

salaries = {}

for emp in employees:
    dept = emp["dept_no"]
    salary = emp["salary"]
    if dept not in salaries:
        salaries[dept] = []
    salaries[dept].append(salary)

for dept, salaries in salaries.items():
    print(f"Dept {dept}: Min Salary = {min(salaries)}, Max Salary = {max(salaries)}")
