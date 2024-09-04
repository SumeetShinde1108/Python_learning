#Constructor  
class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f" HI ! I am {self.name}")
        
per=Person("Sumeet_Shinde")
per.talk()

om=Person("Om Navale")
om.talk()
