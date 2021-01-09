"""
(Guess the Number)
Write a script that plays “guess the number.” Choose the
number to be guessed by selecting a random integer in the range 1 to 1000. Do not reveal
this number to the user. Display the prompt "Guess my number between 1 and 1000 with
the fewest guesses:". The player inputs a first guess. If the guess is incorrect, display
"Too high. Try again." or "Too low. Try again." as appropriate to help the player “zero
in” on the correct answer, then prompt the user for the next guess. When the user enters
the correct answer, display "Congratulations. You guessed the number!", and allow the
user to choose whether to play again.
"""

import random as rand


def play_game(rand_number):
    playerWon = False
    print("Lets play GUESS MY NUMBER!!!")
    while not playerWon:
        # Ask player for correct input
        playerGuess = int(input("Guess my number between 1 to 1000: "))
        while True:
            if playerGuess > 1000 or playerGuess < 1:
                playerGuess = int(input("Number must be between 1 and 1000: "))
            else:
                break
        if playerGuess > rand_number:
            print("Too High. Guess Again")
        elif playerGuess < rand_number:
            print("Too low. Try Again")
        else:
            print("YOU Won")
            print(f"Your number is {playerGuess}\nComputer's number is {rand_number}")
            playerWon = True


while True:
    # Change seed in order to have a random number, seed is there for debugging
    rand.seed(100)
    play_game(rand.randrange(1, 1001))
    try_again = input("Would you like to try again? (Y or N)")
    if try_again == 'Y' or try_again == 'y':
        continue
    elif try_again == 'N' or try_again == 'n':
        break
    else:
        print("Incorrect Input")

print("Thank you for playing")
