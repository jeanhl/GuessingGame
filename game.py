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

while solved == False:
    guess = int(raw_input("Pick a number: "))
    guesses.add(guess)
    if guess > secret_number:
        print "Too high"

    elif guess < secret_number:
        print "Too low"

    else:
        print "You got it! You tried {} times.".format(len(guesses)) 
        solved = True


