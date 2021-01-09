"""
(IPython Session)
Create a list called numbers containing the values from 1 through
15, then use slices to perform the following operations consecutively:
a) Select number’s even integers.
b) Replace the elements at indices 5 through 9 with 0s, then show the resulting list.
c) Keep only the first five elements, then show the resulting list.
d) Delete all the remaining elements by assigning to a slice. Show the resulting list.
"""
numbers = list(range(1, 16))
print(f"Even Integers: {numbers[1::2]}")

# Replace the elements at indices 5 through 9 with 0s, then show the resulting list.
numbers[5:10] = [0] * len(numbers[5:10])
print(f"Replace 5-9 with 0's: {numbers}")

# Keep only the first five elements, then show the resulting list.
numbers[5:] = []
print(f"Keep first 5 elements: {numbers}")
# Delete all the remaining elements by assigning to a slice. Show the resulting list.
numbers[:] = []
print(f"Remove all elements: {numbers}")

"""
(IPython Session2)
Create a list called numbers containing the values from 1 through
15, then use the del statement to perform the following operations consecutively:
a) Delete a slice containing the first four elements, then show the resulting list.
b) Starting with the first element, use a slice to delete every other element of the list,
then show the resulting list.
"""
numbers = list(range(1, 16))
print(f"numbers: {numbers}")

# Delete a slice containing the first four elements, then show the resulting list.
del numbers[0:4]
print(numbers)

# Starting with the first element, use a slice to delete every other element of the list, then show the resulting list.
del numbers[::2]
print(numbers)
