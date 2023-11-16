from functions.printWelcomeMessage import printWelcomeMessage
from handleAskingForWeather import handleAskingForWeather

printWelcomeMessage()

# main menu of instructions for program handling
instruction = None
while(instruction == None or instruction != "q"):
    # Run intro message and get a user instruction
    print("What would you like to do?\n")
    instruction = input("a - ask for the min/max temperatures for a city\nq - quit\n\n")
    if(instruction == "a"):
        handleAskingForWeather()
    elif(instruction == "q"):
        print("\nThank you for using the weather program!\n")
    else:
        print("\nSorry the program doesn't recognise that command yet, please enter either 'a' or 'q'\n")




