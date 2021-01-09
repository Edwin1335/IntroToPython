"""Chapter 4 - Functions"""

# Importing multiple Identifiers from a Module
from math import ceil, floor

ceil(10.3)
floor(10.7)

# Binding names for Modules
import statistics as stats

stats.mean(10, 20)


# Arbitrary Argument List
def average(*args):
    return sum(args) / len(args)


# Passing lists to functions (unpacking)
grades = [88, 75, 96, 55, 83]
print(average(*grades))
