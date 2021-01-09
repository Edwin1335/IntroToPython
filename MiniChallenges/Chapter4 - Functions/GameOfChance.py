"""
You roll two six-sided dice, each with faces containing one, two, three, four, five
and six spots, respectively. When the dice come to rest, the sum of the spots on the
two upward faces is calculated. If the sum is 7 or 11 on the first roll, you win. If
the sum is 2, 3 or 12 on the first roll (called “craps”), you lose (i.e., the “house”
wins). If the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your
“point.” To win, you must continue rolling the dice until you “make your point”
(i.e., roll that same point value). You lose by rolling a 7 before making your point.
"""
import random


def RollDice():
    """Roll the Dice and return a tuple"""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2


def PrintFaces(dieRolls):
    """Print the faces of the rolled dice"""
    die1, die2 = dieRolls
    print(f"Player rolled {die1} + {die2} = {sum(dieRolls)}")
    return sum(dieRolls)


# First Roll
first_roll = PrintFaces(RollDice())

if first_roll in (7, 11):
    player_status = "Won"
elif first_roll in (2, 3, 12):
    player_status = "Lose"
elif first_roll in (4, 5, 6, 8, 9, 10):
    player_status = "Continue"
    print(f"Player must continue player: {first_roll}")

while player_status == "Continue":
    next_roll = PrintFaces(RollDice())

    if next_roll == first_roll:
        player_status = "Won"
    elif int(next_roll) == 7:
        player_status = "Lose"

# Display who won
if player_status == "Won":
    print("Player Won")
else:
    print("Player lost")
