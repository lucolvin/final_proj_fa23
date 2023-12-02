import random
import os

# Global variables
def initializeGlobals():
    # Global variable to check if it is the first time the main loop runs
    global firstTime
    firstTime = True

    # Global variable to count the number of times the player has traveled
    global travelCounter
    travelCounter = 0

    # Global variable to check if it is the first time the player has entered the savannah
    global firstTimeSavannah
    firstTimeSavannah = True
    
    # Global environment variable to init the player's location
    global environment
    environment = 'jungle'

# Call the function to initialize the global variables
initializeGlobals()



# creates a function to clear the screen for linux and windows
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Adds blank lines for readability
    print("\n" * 5)

# clears the screen using clearScreen function on the initial run so the first output will be on a clean screen.
clearScreen()


# Gets the player's playerInput
def getplayerInput():

    # Does not print the first time the main loop runs
    global firstTime, travelCounter, firstTimeSavannah, environment
    if not firstTime:
        travelCounter += 1
        # travelCounter to check the player's location for testing should take out later yo
        print(f"You have traveled {travelCounter} times.")
        if travelCounter <= 20:
            environment = 'jungle'
            print("You are still in a jungle.")
        else:
            if firstTimeSavannah:
                environment = 'savannah'
                print("You are now in a savannah.")
                firstTimeSavannah = False
            else:
                print("You are still in a savannah.")        
        print("You can go north, south, east, or west.")
        print("You can also quit.")
        print("What do you want to do?")
    firstTime = False

    # Player input
    playerInput = input("> ")
    return playerInput



def containsAll(str1, str2):
    # Checks if str1 contains all the letters in str2 to check for playerInput even if the player misspells it
    for letter in str1:
        if letter not in str2:
            return False
    return True

'''
def getCommand(playerInput):
    playerInput = playerInput.lower()
    if containsAll("quit", playerInput) or playerInput == "q":
        return False
    elif containsAll("nor", playerInput) or playerInput == "n":
        clearScreen()
        print("You go north.")
    elif containsAll("sou", playerInput) or playerInput == "s":
        clearScreen()
        print("You go south.")
    elif containsAll("eas", playerInput) or playerInput == "e":
        clearScreen()
        print("You go east.")
    elif containsAll("wes", playerInput) or playerInput == "w":
        clearScreen()
        print("You go west.")
    else:
        clearScreen()
        print("I don't understand that playerInput.")
    return True'''


# TODO make a mini-game that only appears when the player goes a certain direction
# TODO make a river mini-game
# TODO make a mini-game that you need to run away from da ferrel monke
# TODO 

def getCommand(playerInput):
    # Conversion to lowercase
    playerInput = playerInput.lower()

    if containsAll("quit", playerInput) or playerInput == "q":
        clearScreen()
        # Prints the quit message which is different from the death message
        print("\nThanks for playing our game!")
        return False
    

# 1 in 5 chance to trigger the mini-game should be able to just change the 0 of 0, 4 to 1 for other mini-games
# this is dumb what was i thinking facepalm

    elif containsAll("nor", playerInput) or playerInput == "n":
        if random.randint(0, 4) == 0:  # 1 in 5 chance to trigger mini-game

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(environment)
        # Clears the screen using os module
        clearScreen()
        print("You go north.")

    elif containsAll("sou", playerInput) or playerInput == "s":
        if random.randint(0, 4) == 0:  # 1 in 5 chance to trigger the mini-game

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(environment)
        # Clears the screen using os module
        clearScreen()
        print("You go south.")

    elif containsAll("eas", playerInput) or playerInput == "e":
        if random.randint(0, 4) == 0:  # 1 in 5 chance to trigger the mini-game

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(environment)
        # Clears the screen using os module
        clearScreen()
        print("You go east.")

    elif containsAll("wes", playerInput) or playerInput == "w":
        if random.randint(0, 4) == 0:  # 1 in 5 chance to trigger the mini-game

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(environment)
        # Clears the screen using os module
        clearScreen()
        print("You go west.")

    # Its an easter egg ya dingus
    elif containsAll("supersecretsecret", playerInput):
        clearScreen()
        print("you have found the super secret easter egg!!! Have a cookie.")
        print("🍪")
    
    # Exception handling for non-string input
    else:
        clearScreen()
        print("I don't understand that playerInput.")
    return True



# Jungle temple mini-game
def miniGame(environment):
    # Clears the screen using os module
    clearScreen()

    
    # Mini-game introduction
    if environment == 'jungle':
        print("You have encountered a jungle temple! \n\nThe rewards are great but the perils are many.\nOnce you enter you must survive or die.\n\nDo you dare to enter?  (yes/no)")
    
    elif environment == 'savannah':
        print("You have encountered a savannah Oasis! \n\nThe rewards are great but the perils are many.\nOnce you enter you must survive or die.\n\nDo you take the plunge?  (yes/no)") 
    
    # Player input
    while True:
        playGame = input("> ")
        
        # This fixes the bug where the player can enter anything and it will auto win the mini-game
        if playGame.lower() in ['yes', 'y', 'no', 'n']:
            break
        else:
            # Clears the screen using os module
            clearScreen()
            
            # Makes the text stay the same even if the player enters something other than yes or no
            if environment == 'jungle':
                print("You have encountered a jungle temple! \n\nThe rewards are great but the perils are many.\nOnce you enter you must survive or die.\n\nDo you dare to enter?  (yes/no)")
            
            # Makes the text stay the same even if the player enters something other than yes or no
            elif environment == 'savannah':
                print("You have encountered a savannah Oasis! \n\nThe rewards are great but the perils are many.\nOnce you enter you must survive or die.\n\nDo you take the plunge?  (yes/no)") 
            
            # Exception handling for wrong input
            print("Please enter Y/n.")    
            
    # forces input from the player
    if playGame.lower() in ['yes', 'y']:
        
        
        for i in range(5):
            clearScreen()
            print("You are in a jungle temple.")
            print("You can choose between 3 doors.")
            print("Behind up to 2 of the doors is certain death.")
            print("Choose wisely.")
            

            # Randomly chooses 1 or 2 doors to be deadly
            deadlyDoors = random.sample([1, 2, 3], random.randint(1, 2))
            safeDoors = [door for door in [1, 2, 3] if door not in deadlyDoors]
        
        # Player input
            while True:
                try:
                    print("Doors: [1] [2] [3]")  # Visual indication for the doors
                    print(f"Safe doors (for testing): {safeDoors}")  # Marker for the safe doors
                    choice = int(input("> "))
                    if choice in deadlyDoors:
                        # Clears the screen using os module
                        clearScreen()
                        print("\nYou chose poorly. You are dead. GIT GUD!")
                        return False # Game over
                    break
                # exception handling for non-integer input
                except ValueError:
                    print("Please enter a number from 1 to 3.")
                
    
    # Checks if the player does not want to play the mini-game
    elif playGame.lower() in ['no', 'n']:
        # Clears the screen using os module
        clearScreen()
        print("You stumble around the jungle temple and get lost.")
        return True # Game continue
    
    # Clears the screen using os module
    clearScreen()

    # Prints the mini-game win message
    print("You survived the jungle temple and rescued the golden idol.")

    # Prints the return message
    print("You return to the jungle.")
    print("\n" * 1)
    return True




def main():
    # Prints only the first time the main loop runs
    print("thus begins your adventure")
    print("you are in a jungle")
    print("you can go north, south, east, or west")
    print("you can also quit")
    
    # Main loop
    while True:
        playerInput = getplayerInput()
        # Ends the game if the player has traveled 100 times
        if travelCounter >= 99:
            # Clears the screen using os module
            clearScreen()
            # I was gonna say you won but thought it would be funnier to say you died of exhaustion
            print("You have traveled too far and died of exhaustion.")
            break
        if not getCommand(playerInput):
            break
    # Prints Game Over in ascii art with color
    print("""\033[1;33;34m
   _____          __  __ ______    ______      ________ _____  _ 
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \| |
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /| |
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \|_|
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_(_) """ )


main()
