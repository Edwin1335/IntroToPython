import numpy as np


# Create a 2-by-5 array containing the even integers from 2 through
# 10 in the first row and the odd integers from 1 through 9 in the second row.
def challenge_one():
    numbers = np.array([[x for x in range(2, 11, 2)], [x for x in range(1, 10, 2)]])
    print(numbers)


# create an array of twelve random grades in the range 60 through 100, 
# then reshape the result into a 3-by-4 array. Calculate the average of all 
# the grades, the averages of the grades in each column and
# the averages of the grades in each row.
def challenge_two():
    num_array = np.random.randint(60, 101, 12).reshape(3, 4)
    print(num_array.mean(axis=0))


def main():
    # Creating an array
    challenge_two()


main()
