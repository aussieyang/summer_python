# Let's make Hangman
import random

HANGMANPICS = ['''
 +---+
 |   |
     |
     |
     |
     |
=========''','''
 +---+
 |   |
 O   |
     |
     |
     |
=========''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''','''
 +---+
 |   |
 O   |
 |\  |
     |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


#function to display the picture and any incorrect guesses and blanks
def displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord):
    print(HANGMANPICS[len(missedLetters)])
    print("You have taken %d incorrect guesses." % len(missedLetters))
    #loop through all the missed letters and print them out
    for letter in missedLetters:
        print letter
    #variable to hold onto blanks
    blanks = '_' * len(myWord)
    #print out any correct guesses and replace the blank with it
    for i in range(len(myWord)):
        if myWord[i] in correctLetters:
            blanks = blanks[:i] + myWord[i] + blanks[i+1:]
    print blanks

#function to get a guess from the user
def getGuess(alreadyGuessed):
    while True:
        guess = raw_input("Guess a letter >>")
        guess = guess.lower()
        if len(guess) != 1:
            print "Please guess one letter!"
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print "Please guess a letter!"
        elif guess in alreadyGuessed:
            print "You already guessed that letter!"
        else:
            return guess

#function to generate a random word
def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordList.split()) - 1)
    return wordList.split()[wordIndex]

#Set up game variables and inputs
words = "jazzed bopping jinx joke quiz shivving waxes grogginess faking"
print "Let's play some hangman!"
myWord = getRandomWord(words)
gameOver = False
correctLetters = ""
missedLetters = ""

#main loop for the game
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord)
    guess = getGuess(correctLetters + missedLetters)
    #check if the user's guess is correct
    if guess in myWord:
        correctLetters = correctLetters + guess
        #check for whether the player has won
        win = True
        for i in range(len(myWord)):
            if myWord[i] not in correctLetters:
                win = False
                break
            if win:
                print "You win!!"
                gameOver = True
    else:
        missedLetters = missedLetters + guess
        #check for loss
        if len(missedLetters) == len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord)
            print "You lost! The word is %s." % myWord
            gameOver = True

    if gameOver:
        answer = raw_input("Do you want to play again? yes / no >>")
        answer.lower()
        if "yes" in answer:
            myWord = getRandomWord(words)
            gameOver = False
            correctLetters = ""
            missedLetters = ""
        else:
            break



#
