import random

while True:
    print("Welcome to the jungle!")
    print("You are in the jungle. You can go north, south, east, or west.")
    print("You can also quit.")
    print("What do you want to do?")

    command = input("> ")

    if command == "quit":
        break
    elif command == "north":
        print("You go north.")
    elif command == "south":
        print("You go south.")
    elif command == "east":
        print("You go east.")
    elif command == "west":
        print("You go west.")
    else:
        print("I don't understand that command.")
    print()

print("Goodbye!")
