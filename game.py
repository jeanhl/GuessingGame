import random

# Greet player
print "Hello there! Welcome to the guessing game!"
# Get name
name = raw_input("What's your name? ")
print "Hi {}!".format(name)

#picking a random number
secret_number = random.randint(1, 100)
#print secret_number

solved = False

guesses = set()
#this will keep track of number of guesses

while not solved:
    guess = int(raw_input("Pick a number between 1 and 100: "))
    # keeps asking for guesses while not solved; converts to integer
    guesses.add(guess)
    # adds new guess to set of guessed numbers; does not add duplicates

    if guess > secret_number:
        print "Too high."

    elif guess < secret_number:
        print "Too low."

    else:
        print "You got it! You guessed {} numbers.".format(len(guesses)) 
        solved = True
