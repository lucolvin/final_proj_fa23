import random 
import time
#list of words for guessing
def chooseWord():
    words = ["tiger", "snake", "machete", "torch", "banana"]
    return random.choice(words)
#booleans
def displayWord(word, guessedWords):
    display = ""
    for letter in word:
        if letter in guessedWords:
            display += letter
        else:
            display += "_"
    return display 

def clearScreen():
    os('cls' if os.name == 'nt' else 'clear')
    print("\n" * 5)
#hangman attempts
def hangman():
    maxAttempts = 6
    guessedWords = []
    wordsToGuess = chooseWord()
    attemptsLeft = maxAttempts

    print("You stumble upon an ancient tablet!") 
    time.sleep(2)
    print("after further examenation you find out that hang man is older than you think.") 
    time.sleep(4)
    print("you are now playing hangman.")
    time.sleep(3)
    
    while True:
        print("\nAttempts left:", attemptsLeft)
        print(displayWord (wordsToGuess, guessedWords))

        guess = input("Guess a Letter: ").lower()

        if guess in guessedWords:
            print("dont you remember? youve already guessed that!")
            continue 

        guessedWords.append(guess)

        if guess not in wordsToGuess:
            attemptsLeft -= 1
            print("NOPE! try again.")

        if "_" not in displayWord(wordsToGuess, guessedWords):
            print("\nUnfortunetly you won the word is", wordsToGuess)
            break

        if attemptsLeft == 0: 
            print("\nHA you lose! the word was", wordsToGuess)
            break
#call the hangman function
hangman()