try:
    a=int(input("ENter a number:"))
    b=int(input("Enter another number"))
    result = a/b
    print(result)  
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")

