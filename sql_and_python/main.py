import mysql.connector as connector
print("mysql connector imported")

# con = connector.connect(
#     host="localhost",
#     user="root",
#     password="Sheelu@123",
#     database="py_con"
# )
# print("connection etsblished")

class DatabaseConnection:
    def __init__(self):
        self.con = connector.connect(
            host="localhost",
            user="root",
            password="Sheelu@123",
            database="py_con"
        )

        query = "CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY, name VARCHAR(100), age INT)"
        cur = self.con.cursor()
        cur.execute(query)
        print("Table 'students' ensured to exist")

    def insert(self, id, name, age):
        query = "INSERT INTO students(id, name, age) VALUES (%s, %s, %s)"
        values = (id, name, age)
        cur = self.con.cursor()
        cur.execute(query, values)
        self.con.commit()
        print("Values inserted")

    def update(self, id, name, age):
        query = "UPDATE students SET id = %s, name = %s WHERE age = %s"
        values = (id, name, age)
        cur = self.con.cursor()
        cur.execute(query, values)
        self.con.commit()
        print("Record updated")


    def show(self):
        query = "SELECT * FROM students"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

        print("\nID  Name     Age")
        print("-" * 20)
        for row in rows:
            print(row)

    def delete(self, id):
        query = "DELETE FROM students WHERE id = %s"
        values = (id,)
        cur = self.con.cursor()
        cur.execute(query, values)
        self.con.commit()

        if cur.rowcount == 0:
            print("No record found with this ID")
        else:
            print("Record deleted")


    # def delete(self):
    #     query = "DROP DATABASE py_con"
    #     cur = self.con.cursor()
    #     cur.execute(query)
    #     print("databse deleted")

db = DatabaseConnection()
# db.insert(103, "harshit", 28)
# db.show()
# db.delete()



