from main import AdmissionDB

db = AdmissionDB()
while True:
    print("1. Add Student \n")
    print("2. Apply for Admission\n")
    print("3. View Applications\n")
    print("4. Approve Application\n")
    print("5. Reject Application\n")
    print("6. Exit\n")


    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        city = input("City: ")
        db.add_student(name, email, phone, city)

    elif choice == "2":
        student_id = int(input("Student ID: "))
        course = input("Course: ")
        marks = int(input("Marks: "))
        db.apply_for_admission(student_id, course, marks)

    elif choice == "3":
        db.view_all_applications()

    elif choice == "4":
        app_id = int(input("Application ID: "))
        db.update_status(app_id, "Approved")

    elif choice == "5":
        app_id = int(input("Application ID: "))
        db.update_status(app_id, "Rejected")

    elif choice == "6":
        db.close()
        print("Exiting...")
        break

    else:
        print("Invalid choice")

# db = AdmissionDB()