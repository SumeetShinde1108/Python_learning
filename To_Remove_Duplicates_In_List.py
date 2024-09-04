# TO  remove duplicates from the list. 
numbers=[2,3,42,2,43,3,23,2,3,3,4,4,3,3,4,54,3,3,3,4,43,3,23,34,43,4,4,54,5,4,4,5,4,43,4,4,3,43,4,3,4.4,3,4,4,43,4,4,34,3,3,3,3,3,3]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)
