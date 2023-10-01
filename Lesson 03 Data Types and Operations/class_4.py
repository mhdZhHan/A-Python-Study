# Split and Join

# ========================= 1. Split ============================

my_str = "Hello World"

# split the string into a list where each word is a list item
print(my_str.split()) # ['Hello', 'World']

# split the string using 'Wo' as a separator
print(my_str.split("Wo")) # ['Hello ', 'rld']

characters = "Motu, Patlu, Jon"

# split the string, using 'comma', followed by a space, as a separator 
print(characters.split(",")) # ['Motu', 'Patlu', 'Jon']

# ========================= 1. Join ============================

my_list = ["Hello", "World"]

# Join all items in a list into a string, using a tab space as separator
new_str = " ".join(my_list)
print(new_str) # "Hello World"

fruits = ["apple", "orange", "grapes"]

# Join all items in a list into a string, using 'comma' as separator
fruits_str = ",".join(fruits)
print(fruits_str) # "apple,orange,grapes"