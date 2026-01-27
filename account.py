class Bank_Accounts:
    def __init__(self, name, age):
        self.name = name
        self.amount = 10000
        self.age = age
        
        while(True):
            operation = int(input("1. withdraw\n2. Deposit\n3. Show Balance\n4. Exit\nEnter operation:- "))
            if(operation==1):
                a = int(input("Enter the amount you want to withdraw;-"))
                self.amount=self.amount-a
                print("Transection Successfull")
            elif(operation==2):
                a = int(input("Enter the amount you want to deposit;-"))
                self.amount=self.amount+a
                print("Transection Successfull")
            elif(operation==3):
                print(f"{self.name} your account balance is {self.amount}")
            elif(operation==4):
                break
            else:
                print("Invalid operation")
        
    
Bank = Bank_Accounts("Sheelendra", 19)