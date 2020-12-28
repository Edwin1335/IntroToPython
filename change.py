'''
Write a script that inputs a
purchase price of a dollar or less for an item. Assume the purchaser pays with a dollar bill.
Determine the amount of change the cashier should give back to the purchaser. Display
the change using the fewest number of pennies, nickels, dimes and quarters. For example,
if the purchaser is due 73 cents in change, the script would output:
Your change is:
2 quarters
2 dimes
3 pennies
'''

# Variables needed
quarters = 0
nickles = 0
dimes = 0
pennies = 0

# Constant values
quarter_value = .25
penny_value = .01
nickel_value = .05
dime_value = .10


# Get the chenge from the user 
change = float(input("What is the total change: "))

# Get the number of quartes
quarters = int(change // quarter_value)
change = change - (quarter_value * quarters)

# Get the number of dimes
dimes = int(change // dime_value)
change = change - (dime_value * dimes)

# Get the number of dimes
nickles = int(change // nickel_value)
change = change - (nickel_value * nickles)

# Get the number of dimes
pennies = int(round(change / penny_value))
change = change - (penny_value * pennies)

# Output answer
print(f"Your Change is : \nQuarters: {quarters} \nDimes: {dimes:} \nNikles: {nickles} \nPennies: {pennies}")