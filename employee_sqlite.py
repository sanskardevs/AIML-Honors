
import sqlite3


class Employee:
    def __init__(self):
        self.con = sqlite3.connect("employee.db")
        self.cur = self.con.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY,
                name TEXT,
                salary REAL,
                department TEXT
            )
        """)
        self.con.commit()

    # Create
    def add_employee(self):
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        department = input("Enter department: ")

        try:
            self.cur.execute(
                "INSERT INTO employee VALUES (?, ?, ?, ?)",
                (emp_id, name, salary, department)
            )
            self.con.commit()
            print("Employee added successfully")

        except sqlite3.IntegrityError:
            print("Employee ID already exists")

    # Read
    def display_employee(self):
        self.cur.execute("SELECT * FROM employee")
        records = self.cur.fetchall()

        if records:
            for record in records:
                print(record)
        else:
            print("No employee records found")

    # Search
    def search_employee(self):
        emp_id = int(input("Enter employee ID: "))

        self.cur.execute(
            "SELECT * FROM employee WHERE id = ?",
            (emp_id,)
        )
        record = self.cur.fetchone()

        if record:
            print(record)
        else:
            print("Employee not found")

    # Update
    def update_employee(self):
        emp_id = int(input("Enter employee ID to update: "))

        self.cur.execute(
            "SELECT * FROM employee WHERE id = ?",
            (emp_id,)
        )

        if not self.cur.fetchone():
            print("Employee not found")
            return

        name = input("Enter new name: ")
        salary = float(input("Enter new salary: "))
        department = input("Enter new department: ")

        self.cur.execute("""
            UPDATE employee
            SET name = ?, salary = ?, department = ?
            WHERE id = ?
        """, (name, salary, department, emp_id))

        self.con.commit()
        print("Employee updated successfully")

    # Delete
    def delete_employee(self):
        emp_id = int(input("Enter employee ID to delete: "))

        self.cur.execute(
            "DELETE FROM employee WHERE id = ?",
            (emp_id,)
        )
        self.con.commit()

        if self.cur.rowcount > 0:
            print("Employee deleted successfully")
        else:
            print("Employee not found")

    # Close database connection
    def close(self):
        self.con.close()


# Main program
emp = Employee()

try:
    while True:
        print("\n===== EMPLOYEE MANAGEMENT =====")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                emp.add_employee()
            elif choice == 2:
                emp.display_employee()
            elif choice == 3:
                emp.search_employee()
            elif choice == 4:
                emp.update_employee()
            elif choice == 5:
                emp.delete_employee()
            elif choice == 6:
                print("Program ended")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter valid numeric input")

finally:
    emp.close()
