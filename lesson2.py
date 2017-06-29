#Guessing the number game
import random
guessesTaken = 0

myName = raw_input("What's your name >>")
number = random.randint(1, 10)

print "I'm thinking of a number between 1 and 10."

while guessesTaken < 3:
    guess = raw_input("Guess what number >>")
    guess = int(guess)
    guessesTaken += 1   #this means add one to guessesTaken

    if guess < number:
        print "Too low, go higher."
    if guess > number:
        print "Too high, go lower."
    if guess == number:
        break

if guess == number:
    print "Good job, %s, you guessed correctly in %d turns!" % (myName, guessesTaken)
else:
    print "Bad luck, I'm actually thinking of the number %d." % number
