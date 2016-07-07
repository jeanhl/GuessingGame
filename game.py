import random

HIGH_SCORE = 101

def guessing_game(HIGH_SCORE):
    '''Plays a guessing game'''

    #picking a random number
    secret_number = random.randint(1, 100)
    print "The secret number is:",secret_number

    solved = False

    guesses = set()
    #this will keep track of number of guesses

    while not solved:
        guess = raw_input("Pick a number between 1 and 100: ")
        # keeps asking for guesses while not solved

        try:
            guess = int(guess)
        except ValueError:
            print "Please enter an integer."
            continue
            # restarts while loop

        guesses.add(guess)
        # adds new guess to set of guessed numbers; does not add duplicates

        if guess > 100 or guess < 1:
            print "I said between 1 and 100."

        elif guess > secret_number:
            print "Too high."

        elif guess < secret_number:
            print "Too low."

        else:
            print "You got it! You guessed {} numbers.".format(len(guesses))
            # now we will track the high score. 
            # HIGH SCORE is a global variable because it will reset if stored in the function
            if len(guesses) < HIGH_SCORE:
                HIGH_SCORE = len(guesses)
                print "{} is the least amount of numberers guessed!".format(HIGH_SCORE)
            solved = True
    # Asking player if they want to play again 
    again = raw_input("Do you want to play again? (Y/N) ")
    if again == "Y" or again == "y":
        guessing_game(HIGH_SCORE)
    else:
        return

# Greet player
print "Hello there! Welcome to the guessing game!"
# Get name
# name = raw_input("What's your name? ")
# print "Hi {}!".format(name)

guessing_game(HIGH_SCORE)

print "Thank you for playing."

