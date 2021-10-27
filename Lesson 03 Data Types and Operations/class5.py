# Search in a String

string = "pineapple"

# to search the word 'apple' in 'string'
print("apple" in string) # True

# to search the letter 'a' in 'string'
print("a" in string) # True

# to search the word 'orange' in 'string'
print("orange" in string) # False
# ===================================================================================

email = "hello@example.com"

# to search the string 'email' is starts with 'Hello'
print(email.startswith("hello")) # True

# to search the string 'email' is ends with 'Hello'
print(email.endswith("hello")) # False

# to search the string 'email' is ends with '@example.com'
print(email.endswith("@example.com")) # True
# ====================================================================================

fruit = "watermelon"

# to search the string 'fruit' is stars with 'm'
print(fruit.startswith("m")) # False

# to search the string 'fruit' is stars with 'm' & the optional parameter '5' to set start index of the string 'fruit'
print(fruit.startswith("m", 5)) # True

# to search the string 'fruit' is ends with 'o' & '3' to set start index of the string 'fruit'
print(fruit.endswith("o", 3)) # False

# ================================== Find Method =======================================

new_string = "pineapple"

# to find the start position of the word 'apple' in 'new_string'
print(new_string.find("apple")) # 4

# ================================== Index Method =======================================

# to find the start index of the word 'apple' in 'new_string'
print(new_string.index("apple")) # 4

# ================================== Count Method =======================================

# return the number of times the value 'apple' appears in 'new_string'
print(new_string.count("apple")) # 1

print(new_string.count("pp")) # 1

print(new_string.count("p")) # 3