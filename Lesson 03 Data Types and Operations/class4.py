# Split and Join

# ========================= 1. Split ============================

mystr = "Hello World"

# split the string into a list where each word is a list item
print(mystr.split()) # ['Hello', 'World']

# split the string using 'Wo' as a separator
print(mystr.split("Wo")) # ['Hello ', 'rld']

characters = "Motu, Patlu, Jon"

# split the string, using 'comma', followed by a space, as a separator 
print(characters.split(",")) # ['Motu', 'Patlu', 'Jon']

# ========================= 1. Join ============================

mylist = ["Hello", "World"]

# Join all items in a list into a string, using a tab space as separator
newstr = " ".join(mylist)
print(newstr) # "Hello World"

fruits = ["apple", "orange", "grapes"]

# Join all items in a list into a string, using 'comma' as separator
fruits_str = ",".join(fruits)
print(fruits_str) # "apple,orange,grapes"