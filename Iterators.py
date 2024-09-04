mytuple=("banana","apple","pineapple")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
for x in mytuple:
    print(x)
name="Sumeet"
for n in name:
    print(n)

class MyNumbers():
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x= self.a 
        self.a+=1
        return self

myclass=MyNumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))