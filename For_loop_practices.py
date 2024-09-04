#For loop practices
prices=[10,20,30,40,50,60]
total=0
for price in prices:
    total+=price
    print(f"Total is equal to :{total}")


#nested For_Loop
numbers=[5,2,5,2,2]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output+='x'
        print(output)


#List, program to find the largest number

numbers=[325,67,76,46,34,54,35,345,34,53,5,3245,345,23,23,5,4356,45,23,54,345,345,43,23,45,345,34,5]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(f'Largest number is :{ max}')
