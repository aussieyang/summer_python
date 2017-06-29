# Madlibs:
# 1. Create a few variables that get certain bits of info from the user
# 2. Print out a string with a short story, using the info gathered
name = raw_input("What is your name >>")
animal = raw_input("What is your fave animal >>")

story = "Once there lived a boy called %s. His dream was to be a %s trainer." % (name, animal)

print story
