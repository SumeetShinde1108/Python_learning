
#if else statements

temp=(int(input("Enter the temprature")))
if temp>35:
    print("It's a hot day")
elif temp>25 and temp<35:
    print("It,s a good day")
elif temp<25:
    print("It's a cold day")
else:
    print("Don't forget to take sweater with you")


#if else statement with string conditions
name="mosh"
if len(name)<3:
    print("Name at least of 3 characters")
elif len(name)>50:
    print("Name must be maximum of 50 chracters ")
else:
    print("Name looks good ")
