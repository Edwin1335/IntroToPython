"""
At a university, each student is assigned a system login name, which the student uses to log
into the campus computer system. As part of your internship with the university’s Information Technology department,
you have been asked to write the code that generates system
login names for students. You will use the following algorithm to generate a login name:
1. Get the first three characters of the student’s first name. (If the first name is less than
three characters in length, use the entire first name.)
2. Get the first three characters of the student’s last name. (If the last name is less than
three characters in length, use the entire last name.)
3. Get the last three characters of the student’s ID number. (If the ID number is less
than three characters in length, use the entire ID number.)
4. Concatenate the three sets of characters to generate the login name.

For example, if a student’s name is Amanda Spencer, and her ID number is ENG6721, her
login name would be AmaSpe721. You decide to write a function named get_login_name
that accepts a student’s first name, last name, and ID number as arguments, and returns the
student’s login name as a string. You will save the function in a module named login.py.
This module can then be imported into any Python program that needs to generate a login
name. Program 8-3 shows the code for the login.py module.
"""


def encode(ID):
    values = [[len(ID[0]) > 3 and ID[0][:3] or ID[0]],
              [len(ID[1]) > 3 and ID[1][:3] or ID[1]],
              [len(ID[2]) > 3 and ID[2][-3:] or ID[2]]]
    return "".join(values[0] + values[1] + values[2])


def main():
    ID = ["Amanda", "Spencer", "ENG6721"]
    print(encode(ID))


main()
