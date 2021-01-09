"""
(Guess-the-Number Modification)
Modify the previous exercise to count the number of guesses the player makes. If
the number is 10 or fewer, display "Either you know the secret or you got lucky!" If the player makes more than 10
guesses, display "You should be able to do better!" Why should it take no more than 10 guesses? Well, with each “good
guess,” the player should be able to eliminate half of the numbers, then half of the remaining numbers, and so on.
Doing this 10 times narrows down the possibilities to a single number. This kind of “halving” appears in many
computer science applications. For example, in the “Computer Science Thinking: Recursion, Searching, Sorting and Big
O” chapter, we’ll present the high-speed binary search and merge sort algorithms, and you’ll attempt the quicksort
exercise—each of these cleverly uses halving to achieve high performance.
"""

import random as rand


def play_game(rand_number):
    playerWon = False
    number_of_guesses = 0
    print("Lets play GUESS MY NUMBER!!!")
    while not playerWon:
        # Ask player for correct input
        playerGuess = int(input("Guess my number between 1 to 1000: "))
        while True:
            if playerGuess > 1000 or playerGuess < 1:
                playerGuess = int(input("Number must be between 1 and 1000: "))
            else:
                break
        number_of_guesses += 1
        if playerGuess > rand_number:
            print("Too High. Guess Again")
        elif playerGuess < rand_number:
            print("Too low. Try Again")
        elif number_of_guesses <= 10:
            print("Either you know the secret or you got lucky!")
            print(f"Your number is {playerGuess}\nComputer's number is {rand_number}")
            playerWon = True
        else:
            print("You should be able to do better!")
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