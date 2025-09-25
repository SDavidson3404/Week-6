import re

# Ask user input
password = input("Please enter your password: ")

# Regular expression for testing password
regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

# Check if password meets requirements
if re.search(regex, password):
    print("Password is strong")
else:
    print("Password is weak and puny")