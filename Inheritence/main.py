# Employee Inheritance Assignment
# Delena Davis

class Employee:
    """Base class for an employee"""

    def __init__(self, fname, lname, emp_id, department, job_title):
        self.fname = fname
        self.lname = lname
        self.emp_id = emp_id
        self.department = department
        self.job_title = job_title

    def display(self):
        """Display basic employee info"""
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")


# 🔹 Subclass 1
class ProductionWorker(Employee):
    """Production worker with shift and hourly pay"""

    def __init__(self, fname, lname, emp_id, department, job_title, shift, hourlyPayRate):
        super().__init__(fname, lname, emp_id, department, job_title)
        self.shift = shift
        self.hourlyPayRate = hourlyPayRate

    def display(self):
        super().display()

        shift_name = {
            1: "First Shift",
            2: "Second Shift",
            3: "Third Shift"
        }.get(self.shift, "Unknown Shift")

        print(f"Shift: {shift_name}")
        print(f"Hourly Pay: ${self.hourlyPayRate}")
        print("-" * 40)


# 🔹 Subclass 2
class ShiftSupervisor(Employee):
    """Shift supervisor with salary and bonus"""

    def __init__(self, fname, lname, emp_id, department, job_title, annualSalary, bonus):
        super().__init__(fname, lname, emp_id, department, job_title)
        self.annualSalary = annualSalary
        self.bonus = bonus

    def display(self):
        super().display()
        print(f"Annual Salary: ${self.annualSalary}")
        print(f"Bonus: ${self.bonus}")
        print("-" * 40)


# 🔥 DEMONSTRATION PROGRAM
def main():
    print("\n📋 Employee Demonstration\n")

    # Base Employee
    emp = Employee("John", "Doe", "101", "IT", "Technician")
    emp.display()
    print("-" * 40)

    # Production Worker
    worker = ProductionWorker("Sara", "Lee", "102", "Production", "Assembler", 2, 22.50)
    worker.display()

    # Shift Supervisor
    supervisor = ShiftSupervisor("Mike", "Brown", "103", "Production", "Supervisor", 65000, 5000)
    supervisor.display()


if __name__ == "__main__":
    main()