import random


def getCommand():
    print("You are in a jungle.")
    print("You can go north, south, east, or west.")
    print("You can also quit.")
    print("What do you want to do?")

    # Player input
    command = input("> ")
    return command

def containsAll(str1, str2):
    # Checks if str1 contains all the letters in str2 to check for commands even if the player misspells them
    for letter in str1:
        if letter not in str2:
            return False
    return True

'''
def processInput(command):
    command = command.lower()
    if containsAll("quit", command) or command == "q":
        return False
    elif containsAll("nor", command) or command == "n":
        print("\n" * 40)
        print("You go north.")
    elif containsAll("sou", command) or command == "s":
        print("\n" * 40)
        print("You go south.")
    elif containsAll("eas", command) or command == "e":
        print("\n" * 40)
        print("You go east.")
    elif containsAll("wes", command) or command == "w":
        print("\n" * 40)
        print("You go west.")
    else:
        print("\n" * 40)
        print("I don't understand that command.")
    return True'''


def processInput(command):

    # Conversion to lowercase
    command = command.lower()

    if containsAll("quit", command) or command == "q":
        return False
    

# 1 in 5 chance to trigger the mini-game should be able to just change the 0 of 0, 4 to 1 for other mini-games

    elif containsAll("nor", command) or command == "n":
        if random.randint(0, 4) == 0:  # 1 in 5 chance to trigger mini-game
            return miniGame()
        # Clears the screen
        print("\n" * 40)
        print("You go north.")

    elif containsAll("sou", command) or command == "s":
        if random.randint(0, 4) == 0:  # 1 in 5 chance to trigger the mini-game
            return miniGame()
        # Clears the screen
        print("\n" * 40)
        print("You go south.")

    elif containsAll("eas", command) or command == "e":
        if random.randint(0, 4) == 0:  # 1 in 5 chance to trigger the mini-game
            return miniGame()
        # Clears the screen
        print("\n" * 40)
        print("You go east.")

    elif containsAll("wes", command) or command == "w":
        if random.randint(0, 4) == 0:  # 1 in 5 chance to trigger the mini-game
            return miniGame()
        # Clears the screen
        print("\n" * 40)
        print("You go west.")
    
    # Exception handling for non-string input
    else:
        print("\n" * 40)
        print("I don't understand that command.")
    return True

def miniGame():
    # Clears the screen
    print("\n" * 40)

    # Mini-game introduction
    print("You have encountered a jungle temple! The rewards are great but the perils are many.\n Would you like to enter?  (yes/no)")
    playGame = input("> ")
    
    # Checks if the player wants to play the mini-game
    if playGame.lower() in ['yes', 'y']:
        for i in range(5):
            print("\n" * 40)
            print("You are in a jungle temple.\n")
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
                        print("\nYou chose poorly. You are dead.")
                        return False
                    break

            # exception handling for non-integer input
                except ValueError:
                    print("Please enter a number from 1 to 3.")
    elif playGame.lower() in ['no', 'n']:
        return True

    
    # Clears the screen
    print("\n" * 40)
    print("You survived the jungle temple and rescued the golden idol.")
    print("You return to the jungle.")
    print("\n" * 1)
    return True

def main():
    while True:
        command = getCommand()
        if not processInput(command):
            break
    print("\nGame Over!")
    print("GIT GUD!")

main()
