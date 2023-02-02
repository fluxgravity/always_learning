#! python 3
# strongPassword.py - Validates the strength of a password.

def strongPassword():
    import re

    passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    
    while True:
        password_valid = passwordRegex.search(input("Please enter a password (8+ char, uppercase, lower case, 1+ digit): "))

        if password_valid == None:
            print('Password is weak.')
        else:
            print('Password stronk!')
            break

strongPassword()