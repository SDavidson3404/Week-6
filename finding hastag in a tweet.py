import re

# Ask input from user
tweet = input("Please enter a tweet you would like to extract the hashtags from: ")

# Searches for hashtags with a regex
hashtags = re.findall(r"#\w+", tweet)

# Print the results
print(hashtags)