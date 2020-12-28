'''
(IPython Session) Create a function named calculate_product that receives an 
arbitrary argument list and returns the product of all the arguments.
Call the function with the arguments 10, 20 and 30, then with the sequence of 
integers produced by range(1, 6, 2). 
'''
def calculate_product(*args):
    product = 1
    for x in args:
        product *= x
    return product

print("The product is " + str(calculate_product(2,3,4)))

touple = range(1,6,2)

print("The product is " + str(calculate_product(*touple)))
