#while loop and simple game to guess the secrete number
i=1
while i<=5:
    print("*"*i)
    i+=1

secret_no=6
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=(int(input("Guess:")))
    guess_count+=1
    if guess==secret_no:
        print("You won.")
        break
else:
    print("Sorry! You failed ")
