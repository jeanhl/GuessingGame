# Greet player
print "Hello there! Welcome to the guessing game!"
# Get name
name = raw_input("What's your name? ")
print "Hi {}!".format(name)

#picking a random number
import random
secret_number = random.randint(1, 100)
print secret_number
