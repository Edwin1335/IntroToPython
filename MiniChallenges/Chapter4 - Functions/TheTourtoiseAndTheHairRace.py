"""
(Simulation: The Tortoise and the Hare) In this problem, you’ll re-create the classic race of the tortoise and the hare.
You’ll use random-number generation to develop a simulation of this memorable event.
Our contenders begin the race at square 1 of 70 squares. Each square represents a
position along the race course. The finish line is at square 70. The first contender to reach
or pass square 70 is rewarded with a pail of fresh carrots and lettuce. The course weaves its
way up the side of a slippery mountain, so occasionally the contenders lose ground.

A clock ticks once per second. With each tick of the clock, your application should
adjust the position of the animals according to the rules in the table below. Use variables
to keep track of the positions of the animals (i.e., position numbers are 1–70). Start each
animal at position 1 (the “starting gate”). If an animal slips left before square 1, move it
back to square 1.

Create two functions that generate the percentages in the table for the tortoise and the hare, respectively,
by producing a random integer i in the range 1 ≤ i ≤ 10. In the function for the tortoise, perform a “fast plod” when
1 ≤ i ≤ 5, a “slip” when 6 ≤ i ≤ 7 or a “slow plod” when 8 ≤ i ≤ 10. Use a similar technique in the function for the
hare. Begin the race by displaying BANG !!!!! AND THEY'RE OFF !!!!! Then, for each tick of the clock (i.e.,
each iteration of a loop), display a 70-position line showing the letter "T" in the position of the tortoise and the
letter "H" in the position of the hare. Occasionally, the contenders will land on the same square. In this case,
the tortoise bites the hare, and your application should display "OUCH!!!" at that position. All positions other than
the "T", the "H" or the "OUCH!!!" (in case of a tie) should be blank. After each line is displayed, test for whether
either animal has reached or passed square 70. If so, display the winner and terminate the simulation. If the
tortoise wins, display TORTOISE WINS!!! YAY!!! If the hare wins, display Hare wins. Yuck. If both animals win on the
same tick of the clock, you may want to favor the tortoise (the “underdog”), or you may want to display "It's a tie".
If neither animal wins, perform the loop again to simulate the next tick of the clock. When you’re ready to run your
application, assemble a group of fans to watch the race. You’ll be amazed at how involved your audience gets!
"""
import random
import time


def BeginRacing():
    print("BANG !!! \nAND THEY ARE OFF !!!")
    rabbit_position = 1
    tortoise_position = 1
    # Run until either the hair or tortoise reach the finish line
    while rabbit_position < 70 and tortoise_position < 70:
        rabbit_position += UpdateRabbitsPos()
        tortoise_position += UpdateTortoisePos()
        # We dont want to subtract if they both reached the finish line together
        if rabbit_position == tortoise_position and rabbit_position < 70:
            print("OUCH")
            rabbit_position -= 1
        if rabbit_position < 1:
            rabbit_position = 1
        if tortoise_position < 1:
            tortoise_position = 1
        time.sleep(.2)
        print(f"T = {tortoise_position} \nH = {rabbit_position}")
    # Print the winner of the race
    if rabbit_position >= 70 and tortoise_position >= 70:
        print("Its a tie")
    elif rabbit_position >= 70:
        print(" Hare wins. Yuck.")
    else:
        print("TORTOISE WINS!!! YAY!!!")


def UpdateRabbitsPos():
    next_pos = random.randrange(1, 11)
    # Get the next position using the random values
    if 1 <= next_pos <= 2:
        print(f"Rabbit rolls a {next_pos} 'Rabbit Sleeps'")
        return 0
    elif 3 <= next_pos <= 4:
        print(f"Rabbit rolls a {next_pos} 'Big Hop'")
        return 9
    elif next_pos == 5:
        print(f"Rabbit rolls a {next_pos} 'Big Slip'")
        return -12
    elif 6 <= next_pos <= 8:
        print(f"Rabbit rolls a {next_pos} 'Small hop'")
        return 1
    else:
        print(f"Rabbit rolls a {next_pos} 'Small slip'")
        return -2


def UpdateTortoisePos():
    next_pos = random.randrange(1, 11)
    # Get the next position using the random values
    if 1 <= next_pos <= 5:
        print(f"Tortoise rolls a {next_pos} 'Fast Plod'")
        return 3
    elif 6 <= next_pos <= 7:
        print(f"Tortoise rolls a {next_pos} 'Slip'")
        return -6
    else:
        print(f"Tortoise rolls a {next_pos} 'Slow Plod'")
        return 1


BeginRacing()
