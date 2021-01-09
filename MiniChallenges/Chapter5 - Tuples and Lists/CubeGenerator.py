"""
(Cube Generator)
Create a generator expression that cubes the even integers in a list
containing 10, 3, 7, 1, 9, 4 and 2. Use function list to create a list of the results. Note
that the function call’s parentheses also act as the generator expression’s parentheses.
"""
my_list = [10, 3, 7, 1, 9, 4, 2]

new_even_list = list(x ** 3 for x in my_list if x % 2 == 0)
print(new_even_list)
