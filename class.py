# class Students:
#     name = "Sheelendra"
#     grade = 90
#     pass
# student1 = Students()
# print(student1.name)
# print(student1.grade)
# student2 = Students()
# print(student2.name)
# print(student2.grade)

# class Person:
#   def __init__(self, name, age):
#     self.name=name
#     self.age = age

# p1 = Person("Sheelendra", 19)
# print(p1.name)
# print(p1.age)

# class Car:
#     def __init__(self, color, door):
#         self.color=color
#         self.door=door
#     def start(self):
#         print("color with color", self.color)
#     def start2(self):
#         print("Car with doors", self.door)

# c1 = Car("red", 4)
# c1.start
# c1.start2
# ----------------------------------------------
# class Bank_Accounts:
#     def __init__(self, name, age):
#         self.name = name
#         self.amount = 10000
#         self.age = age
        
#         while(True):
#             operation = int(input("1. withdraw\n2. Deposit\n3. Show Balance\n4. Exit\nEnter operation:- "))
#             if(operation==1):
#                 a = int(input("Enter the amount you want to withdraw;-"))
#                 self.amount=self.amount-a
#                 print("Transection Successfull")
#             elif(operation==2):
#                 a = int(input("Enter the amount you want to deposit;-"))
#                 self.amount=self.amount+a
#                 print("Transection Successfull")
#             elif(operation==3):
#                 print(f"{self.name} your account balance is {self.amount}")
#             elif(operation==4):
#                 break
#             else:
#                 print("Invalid operation")
        
    
# Bank = Bank_Accounts("Sheelendra", 19)


class Employee:
    def __init__(self, name, salary, empID):
        self.name=name
        self.salary=salary
        self.empID= empID

    def ann_Salary(self):
        print(f"{self.name}'s Annual Salary is {self.salary*12}")
    
    def work_day(self):
        perday = self.salary/30
        workingDays = int(input("Total Working days:- "))
        print(f"Salary of {workingDays} worinkg is {perday*workingDays}")


E1 = Employee("Harsh", 40000, 12322)

E1.ann_Salary()
E1.work_day()