"""
Collections are prepackaged data structures consisting of related dat items.
List are modifiable, tuples are not.
Lists typically store homogeneous data, that is, values of the same data type.
"""
# Creating a single-element tuple (notice the comma)
single = (123.45, )
print(single)

# Appending Tuples to lists
numbers = [1, 2, 3, 4, 5]
numbers += (6, 7)
print(numbers)

# Tuples may contain mutable objects
student_tuple = ('Amanda', 'Blue', [98, 75, 87])
student_tuple[2][1] = 85
print(student_tuple)

# Create a list/tuple containing enumerates results
colors = ['red', 'green', 'black']
li = list(enumerate(colors))
tu = tuple(enumerate(colors))
for index, value in enumerate(colors):
    print(f'{index}: {value}')

# Creating a bar chart
numbers = [19, 3, 15, 7, 11]
print("\nCreating a bar chart:")
print(f'Index{"Value":>8}{"Bar":>8}')
for index, value in enumerate(numbers):
    print(f"{index:>5}{value:>8}     {'*' * value}")


"""
Sequence Slicing
    You can slice sequences to create new sequences of the same type containing subsets of the
    original elements. 
"""
# Specify a slice
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(f"numbers: {numbers}")
print(f"numbers[2:6]: {numbers[2:6]}")
print(f"numbers[:6]: {numbers[:6]}")
print(f"numbers[6:]: {numbers[6:]}")
print(f"numbers[:]: {numbers[:]}")

# Slicing with steps
print(f"numbers[::2]: {numbers[::2]}")

# Modifying list via slices
numbers[0:3] = ["two", "three", "five"]
print(f"numbers: {numbers}")

# Deleting all the elements (different from assigning a new empty list)
numbers[:] = []
print(f"numbers: {numbers}")


"""
del Statements 
    Can be used to remove elements from a list and to delete variables
    from the interactive session. 
"""
# Deleting and element from a specific index
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
del numbers[-1]
print(numbers)

# Deleting a slice from a list
del numbers[0:2]
print(numbers)

# Deleting entire list vs Deleting entire variable
del numbers[:]
print(numbers)
del numbers
# print(numbers)

"""
Filter and Map list functions
"""
my_list = list(range(1, 31))
print(f"myList: {my_list}")

# Print a list of all squared even numbers
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, my_list))))

# Map a list of Fahrenheit temperatures
fahrenheit = [41, 32, 212]
temp = list(map(lambda x: (x, (x - 32) * 5 / 9), fahrenheit))
print(temp)

# Zip function
names = ["Bob", "Sue", "Amanda"]
grade = [3.5, 4.0, 3.75]
for name, gpa in zip(names, grade):
    print(f"Name: {name}; GPA: {gpa}")
