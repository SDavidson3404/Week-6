import re

# Ask user for input
email = input("Please enter the email you would like to test: ")

# Regular expression to find email
regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Print the result if the email is valid or not
if re.search(regex, email):
    print("Email is valid")
else:
    print("Email is invalid")