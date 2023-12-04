import random
import os

# Hope we can use this
from jungle_lists import directionOutputs

# Global variables
def initializeGlobals():
    
    # Global variable to check if it is the first time the main loop runs
    global firstTime
    firstTime = True

    # Global variables to count the number of times the player has traveled in each direction
    global northCounter, southCounter, eastCounter, westCounter
    northCounter = southCounter = eastCounter = westCounter = 0
    
    # travelCounter to check the player's location for testing should take out later yo
    global travelCounter
    travelCounter = 0


    # Global variable to check if it is the first time the player has entered the savanna
    global firstTimeSavanna
    firstTimeSavanna = True
    
    # Global environment variable to init the player's location
    global environment
    environment = 'jungle'

# Call initializeGlobals() to init the global variables
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
    global firstTime, travelCounter, firstTimeSavanna, environment
    if not firstTime:
        # travelCounter += 1
        # travelCounter to check the player's location for testing should take out later yo
        print(f"\nYou have traveled {travelCounter} times.\n")
        if travelCounter <= 20:
            environment = 'jungle'
            print("You are still in a jungle.")
        else:
            if firstTimeSavanna:
                environment = 'savanna'
                print("You are now in a savanna.")
                firstTimeSavanna = False
            else:
                print("You are still in a savanna.")        
        print("You can go north, south, east, or west.")
        print("You can also quit.")
        print("What do you want to do?")
    firstTime = False

    # Player input uses strip to remove whitespace
    playerInput = input("> ").strip()
    if playerInput: # Fix so travelCounter does not increase when the player enters nothing
        travelCounter += 1
    return playerInput



def containsAll(str1, str2):
    # Checks if str1 contains all the letters in str2 to check if playerInput works even if the player misspells it
    for letter in str1:
        if letter not in str2:
            return False
    return True

# If we have to have only one file we can uncomment this and delete the import and jungle_lists.py file
'''
def directionOutputs():
    northOutputs = [
        "Heading north towards the savanna.",
        "In the distance, the vast savanna awaits to the north.",
        "Towards the north lies the expansive savanna.",
        "Heading northward, the savanna comes into view.",
        "The journey leads north, revealing the open savanna.",
        "To the north, the landscape transitions into a sprawling savanna.",
        "The northern horizon reveals the beauty of the savanna."
    ]

    southOutputs = [
        "Heading south towards the endless ocean.",
        "In the distance, the boundless ocean awaits to the south.",
        "Towards the south lies the vast expanse of the ocean.",
        "Heading southward, the ocean unfolds in the distance.",
        "The journey leads south, revealing the vastness of the ocean.",
        "To the south, the landscape gives way to the expansive ocean.",
        "The southern horizon showcases the endless beauty of the ocean."
    ]

    eastOutputs = [
        "Heading east towards the expansive desert.",
        "In the distance, the vast desert stretches out to the east.",
        "Towards the east lies the endless expanse of the desert.",
        "Heading eastward, the desert unfolds in the distance.",
        "The journey leads east, revealing the arid beauty of the desert.",
        "To the east, the landscape transforms into an expansive desert.",
        "The eastern horizon unveils the beauty of the vast desert."
    ]

    westOutputs = [
        "Heading west towards the towering mountains.",
        "In the distance, the majestic mountains rise to the west.",
        "Towards the west, the towering mountains stand tall.",
        "Heading westward, the mountains come into view.",
        "The journey leads west, revealing the grandeur of the mountains.",
        "To the west, the landscape ascends into the majestic mountains.",
        "The western horizon showcases the beauty of the towering mountains."
    ]
    
    return {"north": northOutputs, "south": southOutputs, "east": eastOutputs, "west": westOutputs}
'''

def getCommand(playerInput):
    
    # calls the global variables
    global northCounter, southCounter, eastCounter, westCounter
    
    # Conversion to lowercase
    playerInput = playerInput.lower()
    
    # Calls directionOutputs() and assigns it to direction
    direction = directionOutputs()
    
    if containsAll("quit", playerInput) or playerInput == "q":
        clearScreen()
        # Prints the quit message which is different from the death message
        print("\nThanks for playing our game!")
        return False
    

    # 1 in 5 chance to trigger the mini-game should be able to just change the 0 of 0, 4 to 1 for other mini-games
    # this is dumb what was i thinking 🤦

    # Changed to 1 in 10 chance to trigger the mini-game so its more rare
    
    elif containsAll("nor", playerInput) or playerInput == "n":
        # Adds 1 to the northCounter
        northCounter += 1
        if random.randint(0, 9) == 0:  # 1 in 10 chance to trigger mini-game

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(environment)
        # Clears the screen using os module
        clearScreen()
        # dont forget the f for an f string
        
        # test for northCounter
        print(f"north test {northCounter} ")
        print(random.choice(direction["north"]))

    elif containsAll("sou", playerInput) or playerInput == "s":
        # Adds 1 to the southCounter
        southCounter += 1
        if random.randint(0, 9) == 0:  # 1 in 10 chance to trigger the mini-game

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(environment)
        
        # Clears the screen using os module
        clearScreen()
        
        # test for southCounter
        print(f"south test {southCounter} ")
        print(random.choice(direction["south"]))# Prints a random output from the list

    elif containsAll("eas", playerInput) or playerInput == "e":
        # Adds 1 to the eastCounter
        eastCounter += 1
        if random.randint(0, 9) == 0:  # 1 in 10 chance to trigger the mini-game

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(environment)
        
        # Clears the screen using os module
        clearScreen()
        
        # test for eastCounter
        print(f"east test {eastCounter} ")
        print(random.choice(direction["east"])) # Prints a random output from the list

    elif containsAll("wes", playerInput) or playerInput == "w":
        # Adds 1 to the westCounter
        westCounter += 1
        if random.randint(0, 9) == 0:  # 1 in 10 chance to trigger the mini-game

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(environment)
        
        # Clears the screen using os module
        clearScreen()
        
        # test for westCounter
        print(f"west test {westCounter} ")
        print(random.choice(direction["west"])) # Prints a random output from the list

    # Its an easter egg ya dingus
    elif containsAll("supersecretsecret", playerInput):
        clearScreen()
        print("you have found the super secret easter egg!!! Have a cookie.")
        print("🍪")
    
    # Exception handling for non-string input
    else:
        clearScreen()
        print("I don't understand that command.")
    return True



# Jungle temple mini-game
def miniGame(environment):
    # Clears the screen using os module
    clearScreen()

    
    # Mini-game introduction
    if environment == 'jungle':
        print("You have encountered a jungle temple! \n\nThe rewards are great but the perils are many.\nOnce you enter you must survive or die.\n\nDo you dare to enter?  (yes/no)")
    
    elif environment == 'savanna':
        print("You have encountered a savanna Oasis! \n\nThe rewards are great but the perils are many.\nOnce you enter you must survive or die.\n\nDo you take the plunge?  (yes/no)") 
    
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
            elif environment == 'savanna':
                print("You have encountered a savanna Oasis! \n\nThe rewards are great but the perils are many.\nOnce you enter you must survive or die.\n\nDo you take the plunge?  (yes/no)") 
            
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
        # Calls getPlayerInput() and assigns it to playerInput
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


# TODO make a mini-game that only appears when the player goes a certain direction
# TODO make a river mini-game
# TODO make a mini-game that you need to run away from da ferrel monke
# TODO make a mini-game that you need to fight da ferrel monke



# TODO Left off working on ints for every direction of travel
