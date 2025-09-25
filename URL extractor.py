import re

# Ask input from user
text = input("Please enter a tweet you would like to extract the hashtags from: ")

# Searches for hashtags with a regex
URLs = re.findall(r"(https?://\S+)", text)

# Print the results
print(URLs)