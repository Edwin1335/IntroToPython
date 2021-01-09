"""
Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers. The program should
store the numbers in a list then display the following data:
•	 The lowest number in the list
•	 The highest number in the list
•	 The total of the numbers in the list
•	 The average of the numbers in the list
"""


def main():
    numbers = []
    for x in range(1, 11):
        numbers.append(int(input(f"{x}: ")))
    print(numbers)
    print(f"Lowest: {min(numbers)}")
    print(f"Highest: {max(numbers)}")
    print(f"Total: {sum(numbers)}")
    print(f"Average: {(sum(numbers) / len(numbers))}")


main()
