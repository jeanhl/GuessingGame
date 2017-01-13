import random

def guessing_game(min_number,max_number,high_score='max_number+1'):
    '''Plays a guessing game'''

    #picking a random number
    secret_number = random.randint(min_number, max_number)
    print "The secret number is:",secret_number

    solved = False

    guesses = set()
    #this will keep track of number of guesses

    while not solved:
        guess = raw_input("Pick a number between {} and {}: ".format(min_number, max_number))
        # keeps asking for guesses while not solved

        try:
            guess = int(guess)
        except ValueError:
            print "Please enter an integer."
            continue
            # restarts while loop

        guesses.add(guess)
        # adds new guess to set of guessed numbers; does not add duplicates

        if guess > max_number or guess < min_number:
            print "I said between {} and {}.".format(min_number, max_number)

        elif guess > secret_number:
            print "Too high."

        elif guess < secret_number:
            print "Too low."

        else:
            print "You got it! You guessed {} numbers.".format(len(guesses))
            # now we will track the high score
            if len(guesses) < high_score:
                high_score = len(guesses)
                print "{} is the least amount of numberers guessed!".format(high_score)
            solved = True
    # Asking player if they want to play again 
    again = raw_input("Do you want to play again? (Y/N) ")
    if lower(again) == "y" :
        guessing_game(min_number,max_number)
    else:
        return

# Greet player
print "Hello there! Welcome to the guessing game!"
# Get name
# name = raw_input("What's your name? ")
# print "Hi {}!".format(name)

guessing_game(1,100)

print "Thank you for playing."

