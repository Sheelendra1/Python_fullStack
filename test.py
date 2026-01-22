
# name = input("Enter name")
# print(name)
# age = int(input("Enter age"))
# print(age)

# marks = float(input("Enter marks"))
# print(marks)

# result = bool(True)
# print(result)


# side = int(input("Enter the side"))
# area = side*side
# print(float(area))

# subj1 = int(input("Enter marks of subj1: "))
# subj2 = int(input("Enter marks of subj2: "))
# subj3 = int(input("Enter marks of subj3: "))
# subj4 = int(input("Enter marks of subj4: "))
# subj5 = int(input("Enter marks of subj5: "))

# total=subj1+subj2+subj3+subj4+subj5
# avg = total/5

# print("Total:- ", total)
# print("Average:- %.2f" %avg)


# bill calculator -------------------------

# itemname
# price 
# quantity
# add total
# gst on total cost;
# then bill

# itemname = input("Enter the item name: ")
# price = int(input("Enter item price: "))
# quantity = int(input("Enter the quantity: "))

# total=price*quantity
# # gst1 = (price*18)/100
# # gstt = gst1*quantity
# # bill = total+gstt
# gst = (total*18)/100
# final_bill = total+gst

# print(final_bill)
# # print(bill)
# print("bill generated with gst")

# operators----------------------

# a = int(input("Enter a number: "))
# b = int(input("Enter second number: "))

# print("Add", a+b)
# print("Sub", a-b)
# print("Mult", a*b)
# print("Div", a/b)

# Daily expanse------------------------

# trex = int(input("Enter travell expense: "))
# food = int(input("Enter food expense: "))
# extra = int(input("Enter extra expense: "))

# Dailytotal=trex+food+extra
# print("daily expense", Dailytotal)

#  calculator---------------------------------

# a = input("Enter a number:- ")
# b = input("Enter another number:- ")

# op = input("Choose operation (+, -, *, /): ")
# if op == "+":
#     result = a + b
# elif op == "-":
#     result = a - b
# elif op == "*":
#     result = a * b
# elif op == "/":
#     result = a/b

# print(result)

# largest number---------------------------------
# a = int(input("First: "))
# b = int(input("Second: "))
# c = int(input("Third: "))

# if a >= b and a >= c:
#     largest = a
# elif b >= a and b >= c:
#     largest = b
# else:
#     largest = c

# print("Largest: ", largest)
 
# password check--------------------------


# Pass="123hh"
# while True:
#     password = input("Enter your password: ")

#     if(Pass==password):
#         print("Access granted")
#         break
#     else:
#         print("access failed")

# Atm---------------------------------------
# Q if amount entered can be break into 200 and 500 notes will discharge 

# amount = int(input("Enter amount"))

# if(amount >=200 and amount%100==0 and amount!=300):
#     print("Discharging cash")
# else:
#     print("Denomination not available")


# greeting according to time take time in 24


time = int(input("Enter hours"))
if 5 <= time < 12:
    print("Good morning")
elif 12 <= time < 17:
    print("Good afternoon")
elif 17 <= time < 21:
    print("Good evening")
elif 0 <= time < 5 or 21 <= time <= 23:
    print("Good night")
else:
    print("enter time b/w 0 to 24")