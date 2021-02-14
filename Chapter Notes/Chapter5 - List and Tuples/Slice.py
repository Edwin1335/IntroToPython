'''
You can slice sequences to create new sequences of the same type containing subsets of the
original elements. Slice operations can modify mutable sequences—those that do not
modify a sequence work identically for lists, tuples and strings.
'''

# Slices create a shallow copy of the object. They copy the elements reference,
# but not the object they point to.


def main():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 64]
    print(f"{'Numbers:':<20} {numbers}")
    print(f"{'numbers[2:6]:':<20} {numbers[2:6]}")
    print(f"{'numbers[2:]:':<20} {numbers[2:]}")
    print(f"{'numbers[:6]:':<20} {numbers[:6]}")
    # Step Slicing
    print(f"\nStep Slicing")
    print(f"{'Numbers:':<20} {numbers}")
    print(f"{'numbers[::2]:':<20} {numbers[::2]}")
    print(f"{'numbers[::-1]:':<20} {numbers[::-1]}")
    numbers.reverse()
    print(f"{'numbers.reverse():':<20} {numbers}")
    numbers.reverse()
    # Modify
    print(f"\nModify List")
    print(f"{'Numbers:':<20} {numbers}")
    print(f"{'numbers[::2]:':<20} {numbers[::2]}")
    print(f"{'numbers[::-1]:':<20} {numbers[::-1]}")


main()
