
# AIML Honors

A collection of assignments, practicals, and projects completed as part of the AIML Honors program.

## 📚 Assignments

### Assignment 1: Multi-Gateway Payment Engine

A Python application demonstrating Object-Oriented Programming (OOP) and the Factory Design Pattern through a simulated payment processing system.

**Features**
- Razorpay and Stripe payment gateways
- Card and UPI payment methods
- Abstract classes and inheritance
- Polymorphism and factory-based object creation
- Basic exception handling

**File:** `multi-gateway-payment-engine.py`

**Run**
```bash
python3 multi-gateway-payment-engine.py
```

---

### Assignment 2: Employee Management System Using CSV

A menu-driven employee management program that performs CRUD operations using Python, Pandas, and CSV file storage.

**Features**
- Add employee records
- Display all employees
- Search employees by ID
- Update employee details
- Delete employee records
- Store records persistently in a CSV file

**Technologies:** Python, Pandas, CSV

**Install dependency**
```bash
python3 -m pip install pandas
```

**Run**
```bash
python3 employee_management.py
```

---

### Assignment 3: Employee Management System Using Database

A menu-driven application that manages employee records in a relational database using Python classes and SQL operations.

**Features**
- Insert employee records
- Display employee records
- Search employees by ID
- Update employee details
- Delete employee records
- Use SQL queries for database operations
- Manage database connections through a Python class

**Technologies:** Python, MySQL, SQL, `mysql-connector-python`

**Install dependency**
```bash
python3 -m pip install mysql-connector-python
```

**Database setup**

Create the database in MySQL:

```sql
CREATE DATABASE employee_db;
```

Configure your MySQL credentials in the Python program before running it.

**Run**
```bash
python3 employee_database.py
```

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming
- Abstraction, inheritance, and polymorphism
- Factory Design Pattern
- Pandas
- CSV file handling
- MySQL and SQL
- Database connectivity

## 🎯 Learning Objectives

- Apply OOP concepts to practical programming problems.
- Create reusable classes and methods.
- Understand abstraction, inheritance, and polymorphism.
- Implement factory-based object creation.
- Perform CRUD operations on CSV files and databases.
- Execute SQL queries using Python.
- Build menu-driven applications with persistent storage.

## 📁 Repository Structure

```text
AIML-Honors/
├── README.md
├── .gitignore
├── multi-gateway-payment-engine.py
├── employee_management.py
└── employee_database.py
```

*Note: Ensure the Assignment 2 and Assignment 3 filenames match the actual files in the repository.*

## 👨‍💻 Author

**Sanskar Amle**

GitHub: [@sanskardevs](https://github.com/sanskardevs)
