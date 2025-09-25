import re

# Ask input from user
text = input("Please enter the string you would like the phone numbers from: ")

# Regular expression to match phone numbers
phone_pattern = r'\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}'

# Extract phone numbers
phone_numbers = re.findall(phone_pattern, text)

print("Extracted Phone Numbers:", phone_numbers)