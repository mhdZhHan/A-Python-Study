# Comparison Operators

x = 10
y = 50

# to check the variable 'x' is less than 'y'
print(x < y) # True

# to check the variable 'x' is gratter than 'y'
print(x > y) # False

# to check the variable 'x' is less than or equalto 'y'
print(x <= y) # True

# to check the variable 'x' is gratter than or equalto'y'
print(x >= y) # False

# to check the variable 'x' is equalto 'y'
print(x == y) # False

# to check the variable 'x' is not equalto 'y'
print(x != y) # True

# ============================= 'in' & 'not' Operator ==============================

# to check the letter 'a' in the word 'apple'
print("a" in "apple") # True

# to check the letter 'a' is not in the word 'apple'
print("a" not in "apple") # False

# ============================= 'is' & 'is not' Operator ==============================

# check the result and get the logic
list1 = ["Helo", "World"]
string = "Hello World"
list2 = string.split()

print("list1: ", list1, "\n" "list2: ",list2)

print(list1 is list2) # False

list1 = list2

print(list1 is list2) # True