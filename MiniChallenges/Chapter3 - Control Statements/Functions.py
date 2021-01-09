import random
import statistics


def square(number):
    # Calculate the square of a number
    return number ** 2


def maximum(number1, number2, number3):
    """Return the maximum of three values"""
    max_value = number1
    if max_value < number2:
        max_value = number2
    if max_value < number3:
        max_value = number3
    return max_value


'''Test the frequency of a six-sided die'''
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

for roll in range(6_000_000):
    face = random.randrange(1, 7)

    # Increment face counters
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency6 += 2

# Print the total frequencies
print(f'Face{"Frequency":>13}')
print(f'{1:>4}{frequency1:>13}')
print(f'{2:>4}{frequency2:>13}')
print(f'{3:>4}{frequency3:>13}')
print(f'{4:>4}{frequency4:>13}')
print(f'{5:>4}{frequency5:>13}')
print(f'{6:>4}{frequency6:>13}')
