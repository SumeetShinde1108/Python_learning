# Exception handling 

try:
    value=int(input("Enter the value"))
    print(f"Value is {value}")
    income=20000
    age=int(input("Enter your age"))
    risk=income/age

except ValueError:
    print("Invalid Value") 

except ZeroDivisionError:
    print("Age can't be 0")
