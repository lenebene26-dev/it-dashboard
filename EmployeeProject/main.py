# Employee Class Assignment
# Delena Davis

class Employee:
    """Class to store employee information"""

    def __init__(self, fname, lname, emp_id, department, job_title):
        self.fname = fname
        self.lname = lname
        self.emp_id = emp_id
        self.department = department
        self.job_title = job_title

    def display(self):
        """Display employee information"""
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print("-" * 40)


def load_employees(filename):
    """Reads employees from file and returns a list of Employee objects"""
    employees = []

    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                # Input validation
                if len(parts) == 5:
                    fname, lname, emp_id, dept, job = parts
                    emp = Employee(fname, lname, emp_id, dept, job)
                    employees.append(emp)

    except FileNotFoundError:
        print("❌ File not found.")

    return employees


def main():
    employee_list = load_employees("employees.txt")

    print("\n📋 Employee List:\n")

    for emp in employee_list:
        emp.display()


if __name__ == "__main__":
    main()