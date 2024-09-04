#Inheritance
class Mammal:
    def talk(self):
        print("It's about the Mammals ")
    def be_annoying(self):
        print("Cat's are so annoying ")
    def bark(self):
        print("Dog's are loyal")


class Dog(Mammal):
   pass


class Cat(Mammal):
   pass

dogs=Dog()
dogs.bark()

cats=Cat()
cats.be_annoying()