#The car game by using the while_loop and if else statement
command=""
started=False
stop=False
while command.upper()!= "QUIT":
    command= input("Enter the command = ").upper()
    if command=="START":  
        if started==True:
            print(">The car has already started!")
        else:
            started=True
            print(">The engine has started ")
    elif command=="STOP":
        if stop==True:
            print(">The engine has already stopped")
        else:    
            stop=True
            print(">The engine has stopped ")   
    elif command=="HELP":
        print('''
        START = To start the engine of the car.
        STOP = To stop the engine of the car.
        QUIT = To quit the game.

        THANK YOU           
        ''')
    elif command=="QUIT":
        print("Thank you for playing the game ")
        break
    else:
        print("Sorry! I don't understand that")