import mysql.connector
from datetime import date

class AdmissionDB:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sheelu@123",
            database="new_db"
        )
        self.cur = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        student_table = """
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            email VARCHAR(50) UNIQUE,
            phone VARCHAR(15),
            city VARCHAR(30)
        )
        """

        application_table = """
        CREATE TABLE IF NOT EXISTS applications (
            application_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT,
            course VARCHAR(50),
            marks INT,
            status VARCHAR(20),
            applied_date DATE,
            FOREIGN KEY (student_id) REFERENCES students(student_id)
        )
        """

        self.cur.execute(student_table)
        self.cur.execute(application_table)
        self.con.commit()

    def add_student(self, name, email, phone, city):
        query = "INSERT INTO students (name, email, phone, city) VALUES (%s, %s, %s, %s)"

        self.cur.execute(query, (name, email, phone, city))
        self.con.commit()
        print("Student added successfully")

    def apply_for_admission(self, student_id, course, marks):
        query = "INSERT INTO applications (student_id, course, marks, status, applied_date) VALUES (%s, %s, %s, %s, %s)"

        self.cur.execute(query, (student_id, course, marks, "Pending", date.today()))
        self.con.commit()
        print("Application submitted")

    def view_all_applications(self):
        query = """
        SELECT a.application_id,
        s.name,
        a.course,
        a.marks,
        a.status,
        a.applied_date
        FROM applications a
        JOIN students s ON a.student_id = s.student_id
        """
        self.cur.execute(query)
        records = self.cur.fetchall()

        for row in records:
            print(row)

    def update_status(self, application_id, status):
        query = "UPDATE applications SET status=%s WHERE application_id=%s"
        
        self.cur.execute(query, (status, application_id))
        self.con.commit()
        print("Application updated")
