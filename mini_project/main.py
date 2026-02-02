import mysql.connector as connector
from datetime import date
print("Connector imported")
class DbConnector:
    def __init__(self):
        self.con = connector.connect(
            host="localhost",
            user="root",
            password="Sheelu@123",
            database="new_db"
        )
        print("database connected")

        query = "CREATE TABLE IF NOT EXISTS students (student_id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), email VARCHAR(50) UNIQUE, phone INT, city VARCHAR(50))"
        cur = self.con.cursor()
        cur.execute(query)
        print("Table 'students' created")


        query1 = "CREATE TABLE IF NOT EXISTS applications (application_id INT PRIMARY KEY AUTO_INCREMENT, student_id INT, course VARCHAR(50), marks INT, status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending', applied_date DATE, FOREIGN KEY (student_id) REFERENCES students(student_id))"
        cur2 = self.con.cursor()
        cur2.execute(query1)
        print("Table 'applications' created")
    def add_student(self, name, email, phone, city):
        query = "INSERT INTO students (name, email, phone, city) VALUES (%s, %s, %s, %s)"
        try:
            self.cur = self.con.cursor()
            self.cur.execute(query, (name, email, phone, city))
            self.con.commit()
            print("Students added")
        except connector.IntegrityError:
            print("Student with this email already exists")
        except Exception as e:
            print(e)

    def apply_for_admission(self, student_id, course, marks, applied_date=None):
        if applied_date is None:
            applied_date = date.today()
        query = "INSERT INTO applications (student_id, course, marks, applied_date) VALUES (%s, %s, %s, %s)"
        self.cur = self.con.cursor()
        self.cur.execute(query, (student_id, course, marks, applied_date))
        self.con.commit()
        print("Application submitted successfully")

    def view_all_applications(self):
        query = """
        SELECT 
            a.application_id,
            s.student_id,
            s.name,
            a.course,
            a.marks,
            a.status,
            a.applied_date
        FROM applications a
        INNER JOIN students s
            ON a.student_id = s.student_id
        """
        self.cur = self.con.cursor()
        self.cur.execute(query)
        rows = self.cur.fetchall()

        print("\nAppID | StuID | Name | Course | Marks | Status | Date")
        print("-" * 75)
        for row in rows:
            print(row)

    def update_status(self, application_id, status):
        query = "UPDATE applications SET status = %s WHERE application_id = %s"
        self.cur = self.con.cursor()
        self.cur.execute(query, (status, application_id))
        self.con.commit()

        if self.cur.rowcount == 0:
            print("Application not found")
        else:
            print(f"Application {status} ")
    
db = DbConnector()