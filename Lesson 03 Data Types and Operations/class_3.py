# Multi-line String && Basic String Methods

# =================================== 1. Multi-line String ( Using Triple Quote) ===========================

greeting = """Hello 
I'am fine"""
print(greeting)

# ================================== 2. Basic String Methods ===============================================

a = "bee String"

# First character capitalized and the rest lowercased.
print(a.capitalize()) # "Bee String"

# String to be all uppercase
print(a.upper()) # "BEE STRING"

# String is in title case
print(a.title()) # "Bee String"

# String’s alphabetic characters are all lower case
print(a.lower()) # "bee string"

# Replace a specified phrase with another specified phrase.
print(a.replace("String", "Strings")) # "bee Strings"

# ==================================================================================

whitespace_string = "     hey      "

# delete spaces from the left side
print(whitespace_string.lstrip()) # "hey      "

# delete spaces from the right side
print(whitespace_string.rstrip()) # "     hey"

# delete spaces from both side
print(whitespace_string.strip()) # "hey"

normal_string = "incomprehensibilities"

# delete all 'i' and 's' from the left side
print(normal_string.lstrip("is")) # "ncomprehensibilities"

# delete all trailing 'i' and 's' from both sides
print(normal_string.rstrip("is")) # "incomprehensibilitie"


word = "Mississippi"

# starting from the right side, all 'i', 'p', and 's' are remove
print(word.rstrip("ips")) # "M"

# the word starts with "M" rather than 'i', 'p', and 's', so nothing to remove
print(word.lstrip("ips")) # "Mississippi"

# 'M', 'i', 'p' and 's' are removed from the both side
print(word.strip("Mips")) # ""