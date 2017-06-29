from sys import exit

# Declare a function called "start" and print out three lines of story
def start():
	print "You are in a abandoned ship."
	print "There is a door to the left and right."
	print "Which one do you take?"
	choice = raw_input("left / right >>")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		print "Please choose left or right."
		start()

def bear_room():
	print "There's a bear in there."
	print "It has some yummy honey and is sitting in front of a door."
	print "How are you going to move the bear?"
	bear_moved = False
	# Write a while loop that repeats forever unless we run dead() or gold_room(). There will be three options - take honey / taunt bear / open door. The play must first taunt the bear before opening the door. All other options lead to death.
	while True:
		choice = raw_input("take honey / taunt bear / open door >>")
		if choice == "take honey":
			dead("The bear slaps your face off. Game over.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved. The door is clear."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear sings you a song so badly you die. Game over.")
		elif choice == "open door" and not bear_moved:
			dead("The bear chews off your left toe. Game over.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "Please choose one of the following:"

def cthulhu_room():
	print "Here you see an evil creature - the Cthulhu."
	print "If he stares at you, you will go insane."
	print "Do you flee for your life or fight the creature?"
	choice = raw_input("flee / fight >>")

	if "flee" in choice:
		start()
	elif "fight" in choice:
		dead("The Cthulhu makes our brain melt. Game over.")
	else:
		print "You feel yourself becoming more insane..."
		cthulhu_room()

def gold_room():
	print "This room is full of gold!"
	print "How much do you take?"
	choice = raw_input("Type a number >>")
	choice = int(choice)

	if choice < 100:
		print "Good job! You are not greedy! You win!"
		exit(0)
	else:
		dead("You are too greedy. You get stuck in the room. Game Over!")

def dead(msg):
	print msg
	exit(0)

start()




	# 