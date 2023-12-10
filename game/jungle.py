import random
import os

# Hope we can use this
# from jungle_lists import directionOutputs

# Global variables
class Game:
    def __init__(self):
        self.firstTime = True
        self.northCounter = 0
        self.southCounter = 0
        self.eastCounter = 0
        self.westCounter = 0
        self.travelCounter = 0
        self.score = 0
        self.multiplier = 1
        # self.firstTimeSavanna = True
        self.miniGameScore = 0
        self.environment = 'jungle'
        
    def increaseMultiplier(self):
        self.multiplier += 10
        return self.multiplier
    
    def decreaseMultiplier(self):
        if self.multiplier > 1:
            self.multiplier -= 1
        return self.multiplier
    
    def updateScore(self, points):
        self.score += points * self.multiplier
        self.miniGameScore += points # updates the miniGameScore
        
    def getMiniGameScore(self):
        return self.getMiniGameScore
    
game = Game()



# creates a function to clear the screen for linux and windows
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Adds blank lines for readability
    print("\n" * 5)

# clears the screen using clearScreen function on the initial run so the first output will be on a clean screen.
clearScreen()


# Gets the player's playerInput
def getPlayerInput(game):
    
    # Does not print the first time the main loop runs
    #firstTime, , southCounter, eastCounter, westCounter, environment
    if not game.firstTime:
        # travelCounter to check the player's location for testing should take out later yo
        print(f"\nYou have traveled {game.travelCounter} times.\n")
        
        # Checks if the player has traveled 20 times in a direction using a conditional statement to move between environments
        if game.northCounter - game.southCounter >= 20:
            print(game.northCounter - game.southCounter)
            game.environment = 'savanna'
            print("You are in a savanna.")
        elif game.southCounter - game.northCounter >= 20:
            game.environment = 'ocean'
            print("You are in a ocean.")
        elif game.eastCounter - game.westCounter >= 20:
            game.environment = 'dessert'
            print("You are in a dessert.")
        elif game.westCounter - game.eastCounter >= 20:
            game.environment = 'mountains'
            print("You are in a mountains.")
        else:
            print("You are still in a jungle.")        
        print("You can go north, south, east, or west.")
        print("You can also quit.")
        print("What do you want to do?")
    game.firstTime = False

    # Player input uses strip to remove whitespace
    playerInput = input("> ").strip()
    if playerInput: # Fix so travelCounter does not increase when the player enters nothing
        game.travelCounter += 1
    return playerInput



def containsAll(str1, str2):
    # Checks if str1 contains all the letters in str2 to check if playerInput works even if the player misspells it
    for letter in str1:
        if letter not in str2:
            return False
    return True

# List of outputs for each direction
def directionOutputs():
    northOutputs = [
        "Heading north towards the savannah.",
        "In the distance, the vast savannah awaits.",
        "Towards the north lies the expansive savannah.",
        "Heading northward, the savannah comes into view.",
        "The journey leads north, revealing the open savannah.",
        "To the north, the landscape transitions into a sprawling savannah.",
        "The northern horizon reveals the beauty of the savannah."
    ]

    southOutputs = [
        "Heading south towards the endless ocean.",
        "In the distance, the boundless ocean awaits.",
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
    # Returns a dictionary with the outputs for each direction
    # Its a dictionary yo
    return {"north": northOutputs, "south": southOutputs, "east": eastOutputs, "west": westOutputs}


def getCommand(playerInput):
    
    # calls the global variables for the directions
    #global northCounter, southCounter, eastCounter, westCounter
    
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
        game.northCounter += 1
        if random.randint(0, 9) == 0:  # 1 in 10 chance to trigger mini-game

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(game)
        # Clears the screen using os module
        clearScreen()
        # dont forget the f for an f string
        
        # test for northCounter
        print(f"north test {game.northCounter - game.southCounter} ")
        print(random.choice(direction["north"]))

    elif containsAll("sou", playerInput) or playerInput == "s":
        # Adds 1 to the southCounter
        game.southCounter += 1
        # 1 in 10 chance to trigger mini-game
        if random.randint(0, 9) == 0:

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(game)
        
        # Clears the screen using os module
        clearScreen()
        
        # test for southCounter
        print(f"south test {game.southCounter - game.northCounter} ")
        print(random.choice(direction["south"]))# Prints a random output from the list

    elif containsAll("eas", playerInput) or playerInput == "e":
        # Adds 1 to the eastCounter
        game.eastCounter += 1
        # 1 in 10 chance to trigger mini-game
        if random.randint(0, 9) == 0:

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(game)
        
        # Clears the screen using os module
        clearScreen()
        
        # test for eastCounter
        print(f"east test {game.eastCounter - game.westCounter} ")
        print(random.choice(direction["east"])) # Prints a random output from the list

    elif containsAll("wes", playerInput) or playerInput == "w":
        # Adds 1 to the westCounter
        game.westCounter += 1
        # 1 in 10 chance to trigger mini-game
        if random.randint(0, 9) == 0:

            # Runs mini-game and checks environment to run the correct mini-game
            return miniGame(game)
        
        # Clears the screen using os module
        clearScreen()
        
        # test for westCounter
        print(f"west test {game.westCounter - game.eastCounter} ")
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
def miniGame(game):
    # Clears the screen using os module
    clearScreen()

    
    # Mini-game introduction
    if game.environment == 'jungle':
        print("You have encountered a jungle temple! \n\nThe rewards are great but the perils are many.\nOnce you enter you must survive or die.\n\nDo you dare to enter?  (yes/no)")
    
    elif game.environment == 'savanna':
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
            if game.environment == 'jungle':
                print("You have encountered a jungle temple! \n\nThe rewards are great but the perils are many.\nOnce you enter you must survive or die.\n\nDo you dare to enter?  (yes/no)")
            
            # Makes the text stay the same even if the player enters something other than yes or no
            elif game.environment == 'savanna':
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
                
    
    # Checks if the player does not want to play the mini-game when in the jungle
    elif playGame.lower() in ['no', 'n'] and game.environment == 'jungle':
        # Clears the screen using os module
        clearScreen()
        print("You stumble around the jungle temple and get lost.")
        return True # Game continue
    
    # Checks if the player does not want to play the mini-game when in the savanna
    elif playGame.lower() in ['no', 'n'] and game.environment == 'savanna':
        # Clears the screen using os module
        clearScreen()
        print("You realize the oasis is a mirage and continue on your journey.")
        return True
    
    # Clears the screen using os module
    clearScreen()

     # Prints the mini-game win message
    game.increaseMultiplier()
    miniGameScore = 50  # You can adjust this based on the difficulty or complexity of the mini-game
    print(f"You survived the jungle temple and rescued the golden idol. You earned {miniGameScore} points.")

    # Updates the overall game score and mini-game score
    game.updateScore(miniGameScore)

    # Prints the return message
    print("You return to the jungle.")
    print("\n" * 1)
    print(f"\nMini-Game Score: {game.getMiniGameScore()}")  # Print mini-game score for verification
    return True


def score(game):
    # Updates the score based on the multiplier
    game.score += 1
    print(f"Score: {game.score * game.multiplier}")

    # Display mini-game score
    miniGameScore = game.getMiniGameScore
    print(f"Mini-Game Score: {miniGameScore}")

    
def main():
    game = Game()
    # Prints only the first time the main loop runs
    print("thus begins your adventure")
    print("you are in a jungle")
    print("you can go north, south, east, or west")
    print("you can also quit")
    
    # Main loop
    while True:
        game = Game()
        print(game.environment)
        score(game)
        # Calls getPlayerInput() and assigns it to playerInput
        playerInput = getPlayerInput(game)
        # Ends the game if the player has traveled 100 times
        if game.travelCounter >= 99:
            # Clears the screen using os module
            clearScreen()
            # I was gonna say you won but thought it would be funnier to say you died of exhaustion
            print("You have traveled too far and died of exhaustion.")
            print(f"your total score is: {game.score * 10}")
            break
        if not getCommand(playerInput):
            break
    # Prints Game Over in ascii art with color
    print("""\033[1;33m
       _____          __  __ ______    ______      ________ _____  _ 
      / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \| |
     | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | |
     | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /| |
     | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \|_|
      \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_(_) 
      
      \033[0m""" )


main()


# TODO make a mini-game that only appears when the player goes a certain direction
# TODO make a river mini-game
# TODO make a mini-game that you need to run away from da ferrel monke
# TODO make a mini-game that you need to fight da ferrel monke



# TODO Left off working on ints for every direction of travel

# TODO make a mini-game that only appears when the player goes a certain direction
