
import pandas as pd
import os


class Employee:
    def __init__(self):
        self.file = "employee.csv"

        if os.path.exists(self.file):
            self.df = pd.read_csv(self.file)
        else:
            self.df = pd.DataFrame(
                columns=["id", "name", "salary", "department"]
            )

    def save(self):
        self.df.to_csv(self.file, index=False)

    # Create
    def add_employee(self):
        emp_id = int(input("Enter employee ID: "))

        if emp_id in self.df["id"].values:
            print("Employee ID already exists")
            return

        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        department = input("Enter department: ")

        new_employee = pd.DataFrame([{
            "id": emp_id,
            "name": name,
            "salary": salary,
            "department": department
        }])

        self.df = pd.concat(
            [self.df, new_employee], ignore_index=True
        )
        self.save()
        print("Employee added successfully")

    # Read
    def display_employee(self):
        if self.df.empty:
            print("No employee records found")
        else:
            print(self.df.to_string(index=False))

    # Search
    def search_employee(self):
        emp_id = int(input("Enter employee ID to search: "))
        result = self.df[self.df["id"] == emp_id]

        if result.empty:
            print("Employee not found")
        else:
            print(result.to_string(index=False))

    # Update
    def update_employee(self):
        emp_id = int(input("Enter employee ID to update: "))

        if emp_id not in self.df["id"].values:
            print("Employee not found")
            return

        name = input("Enter new name: ")
        salary = float(input("Enter new salary: "))
        department = input("Enter new department: ")

        self.df.loc[self.df["id"] == emp_id, "name"] = name
        self.df.loc[self.df["id"] == emp_id, "salary"] = salary
        self.df.loc[self.df["id"] == emp_id, "department"] = department

        self.save()
        print("Employee updated successfully")

    # Delete
    def delete_employee(self):
        emp_id = int(input("Enter employee ID to delete: "))

        if emp_id not in self.df["id"].values:
            print("Employee not found")
            return

        self.df = self.df[self.df["id"] != emp_id]
        self.save()
        print("Employee deleted successfully")



# Main program
emp = Employee()

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
    else:
        print("Invalid choice")

except ValueError:
    print("Please enter a valid number")
