"""
Lo Shu Magic Square
The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-18. The
Lo Shu Magic Square has the following properties:
•	 The grid contains the numbers 1 through 9 exactly.
•	 The sum of each row, each column, and each diagonal all add up to the same number.
In a program you can simulate a magic square using a two-dimensional list.
Write a function that accepts a two-dimensional list as an argument and determines whether the list is
a Lo Shu Magic Square. Test the function in a program
"""


def MagicSquare(grid):
    sum_num = sum(x for x in grid[0])
    print(sum_num)
    for i in grid:
        num_sum = 0
        for j in i:
            if j <= 0 or j >= 10:
                return print(f"{j} is not between 1 and 9")
            num_sum += j
        if num_sum != sum_num:
            return print(f"Numbers dont add up to the same value {num_sum}")


def main():
    grid = [[4, 9, 2],
            [3, 5, 7],
            [8, 1, ]]
    MagicSquare(grid)


main()
