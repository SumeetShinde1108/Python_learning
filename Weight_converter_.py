#program to convert weigth into kgs/lbs

weight=int(input("Enter the weight"))
unit=input("kgs or lbs")
if unit.upper()=="K":
    converted=weight*0.45
    print(f'Weight in kilograms is {converted}')
else:
    converted=weight/0.45
    print(f"weight in pounds {converted}") 