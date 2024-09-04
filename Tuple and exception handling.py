# To define tuple and exception handling  
coordinates=(24,34,44)
x,y,z=coordinates
print(x)
print(y)
print(z)

try:
    coordinates.append(5)
except AttributeError:
    print("Tuple can't be modified") 

