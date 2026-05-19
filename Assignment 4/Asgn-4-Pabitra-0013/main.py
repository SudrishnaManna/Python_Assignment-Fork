class Employee:
    def __init__(self, name, years_of_service):
        self.name = name
        self.years_of_service = years_of_service

    def salary(self):
        return 1500 + 100 * self.years_of_service


class Manager(Employee):
    def salary(self):
        return 2500 + 120 * self.years_of_service


# 1. Create and populate the dictionary-based database
database = {}

samples = [
    Employee('Arijit', 3),
    Employee('Chiku', 1),
    Manager('Sayan', 10),
    Manager('Debu', 3)
]

for emp in samples:
    database[emp.name] = emp

# 2. Build the table as a list of lists [[name, salary]]
salary_table = []
total_salary = 0

for name, emp_object in database.items():
    emp_salary = emp_object.salary()
    salary_table.append([name, emp_salary])
    total_salary += emp_salary

# 3. Compute the average salary
average_salary = total_salary / len(database)

# --- Output Results ---
print("Salary Table:")
print(salary_table)
print(f"\nAverage Salary: {average_salary:.2f}")