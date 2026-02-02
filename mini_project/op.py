from main import DbConnector

db = DbConnector()

while True:
    print("1. Add Student")
    print("2. Apply for Admission")
    print("3. View Applications")
    print("4. Approve Application")
    print("5. Reject Application")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = int(input("Enter Phone: "))
        city = input("Enter City: ")
        db.add_student(name, email, phone, city)

    elif choice == "2":
        student_id = int(input("Enter Student ID: "))
        course = input("Enter Course: ")
        marks = int(input("Enter Marks: "))
        db.apply_for_admission(student_id, course, marks)

    elif choice == "3":
        db.view_all_applications()

    elif choice == "4":
        app_id = int(input("Enter Application ID: "))
        db.update_status(app_id, "Approved")

    elif choice == "5":
        app_id = int(input("Enter Application ID: "))
        db.update_status(app_id, "Rejected")

    elif choice == "6":
        break

    else:
        print("Invalid choice")
