'''Classes and their attributes
#try and except /error handling'''
class Point:
    def huiee(num1,num2):
        print(f"Addition of two numbers:")
        return num1+num2
        
    def butcher(num2,num1):
        print("Subtraction of two numbers")
        return num1-num2
        
point1=Point()                                      #Creating object
point1.a=12
point1.b=11
print(point1.huiee(3,6))                             # Positional argument
print(point1.butcher(num2=455,num1=342))                 # assigned arguments 


try:
    print(point1.c)
except AttributeError:
     print("This can't point1's aqttribute")
try:
    print(point2.a)
except NameError:
    print("Try define object named point2 first")
