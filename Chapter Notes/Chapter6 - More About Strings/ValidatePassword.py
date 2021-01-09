"""
At the university, passwords for the campus computer system must meet the following
requirements:
• The password must be at least seven characters long.
• It must contain at least one uppercase letter.
• It must contain at least one lowercase letter.
• It must contain at least one numeric digit.
When a student sets up his or her password, the password must be validated to ensure it
meets these requirements. You have been asked to write the code that performs this validation.
You decide to write a function named valid_password that accepts the password
as an argument and returns either true or false, to indicate whether it is valid.
"""


def ValidatePassword(password):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if len(password) < 7:
        return False
    for x in password:
        if x.isupper():
            has_uppercase = True
        if x.islower():
            has_lowercase = True
        if x.isdigit():
            has_digit = True
    if has_uppercase and has_lowercase and has_digit:
        return True
    else:
        return False


def encode(ID):
    values = [[len(ID[0]) > 3 and ID[0][:3] or ID[0]],
              [len(ID[1]) > 3 and ID[1][:3] or ID[1]],
              [len(ID[2]) > 3 and ID[2][-3:] or ID[2]]]
    return "".join(values[0] + values[1] + values[2])


def main():
    ID = ["Amanda", "Spencer", "ENG6721"]
    print(ValidatePassword(encode(ID)) and f"Correct Password: {encode(ID)}" or f"Incorrect Password: {encode(ID)}")


main()
