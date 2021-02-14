"""
Two-Dimensional Lists
Lists can contain other lists as elements. A typical use of such nested (or multidimensional)
lists is to represent tables of values consisting of information arranged in rows and columns. 
To identify a particular table element, we specify two indices—by convention, the
first identifies the element’s row, the second the element’s column.
Lists that require two indices to identify an element are called two-dimensional lists
(or double-indexed lists or double-subscripted lists). Multidimensional lists can have
more than two indices. Here, we introduce two-dimensional lists. 
"""


def main():
    a = [[77, 68, 86, 73],  # first student's grades
         [96, 87, 89, 81],  # second student's grades
         [70, 90, 86, 81]]  # third student's grades

    print(f"\nMatrix: {a}")
    for i, row in enumerate(a):
        for j, item in enumerate(row):
            print(f'a[{i}][{j}]= {item} ', end=' ')
        print()

    t = [[10, 7, 3], [20, 4, 17]]
    total = 0
    items = 0
    for i in t:
        for x in i:
            total += x
            items += 1
    print(f"Average: {total/items}")
    total = 0
    items = 0

    for i in t:
        total += sum(i)
        items += len(i)
    print(f"Average: {total/items}")


main()
