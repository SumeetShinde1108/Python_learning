# Functions 
def greet_user(first_name,second_name):
    print(f"HI {first_name }{second_name}!")
    print("Welcome onboard,")

def multiplication(a,b):
    mult=a*b
    print(f"The multiplication of a and b is {mult}")


greet_user('Sumeet','Shinde')
multiplication(34,76) 

#Return functions to return square of a number
def multiplication(number):
    return number*number

print(multiplication(int(input("Enter the number you want get square of it = "))))
