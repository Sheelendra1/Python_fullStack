Mini Project Assignment

College Admission Portal (Python + MySQL)

---
Problem Statement

Design and implement a “College Admission Portal backend”using Python and MySQL

The system should allow:

- Students to apply for admission
- Admin to manage applications
- Data to be stored permanently in a database

You must use Python classes and database connectivity concepts learned in class.

---
 Part A: Database Design (Conceptual)

 Q1.

Create a MySQL database named new_db. --------->\\

Q2.

Design the following tables:

students

| Column | Description |
| --- | --- |
| student_id | Primary key, auto increment |
| name | Student name |
| email | Unique email |
| phone | Contact number |
| city | City |
----------------------------------------->\\
applications

| Column | Description |
| --- | --- |
| application_id | Primary key |
| student_id | Foreign key (students table) |
| course | Course name |
| marks | Student marks |
| status | Pending / Approved / Rejected |
| applied_date | Date of application |
--------------------------------------------------->\\
---

Part B: Python Class (Backend Logic)
 Q3.

Create a Python class named AdmissionDB that:
- Establishes a database connection in __init__
- Creates the required tables if they do not exist

---

 Q4.

Implement the following methods inside the class:

| Method Name | Purpose |
| --- | --- |
| add_student() | Add a new student |
| apply_for_admission() | Insert an admission application |
| view_all_applications() | Display all applications |
| update_status() | Approve or reject an application |
| close() | Close database connection |


 Part C: Control Flow (Main Program)

 Q5.

Create a separate file main.py that:

- Imports the AdmissionDB class
- Displays a menu-driven interface
- Takes user input
- Calls appropriate database methods

 Menu options:


1. Add Student
2. Apply for Admission
3. View Applications
4. Approve Application
5. Reject Application
6. Exit