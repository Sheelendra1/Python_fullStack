from main import DatabaseConnection

def main():
    db=DatabaseConnection()
    while(True):
        print("1. Insert\n")
        print("2. Update\n")
        print("3. Show\n")
        print("4. Delete\n")
        print("5. Exit\n")

        choice = int(input("Enter your choice:-"))
        if choice==1:
            id=int(input("Enter id:-"))
            name= input("Enter name:-")
            age=int(input("Enter age:-"))
            db.insert(id, name, age)

        elif(choice==2):
            id=int(input("Enter id:-"))
            name= input("Enter name:-")
            age=int(input("Enter age:-"))
            db.update(id, name, age)

        elif(choice==3):
            db.show()
        elif(choice==4):
            id=int(input("Enter id:-"))
            db.delete(id)
        elif(choice==5):
            break
        else:
            print("invalid entry")

if __name__=="__main__":
    main()
# helper = DBHelper()