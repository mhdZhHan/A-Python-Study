# Tuple Operations 2.0

# tuple is using as a dictionary key
names = ("a", "b")
student = {}
student[names] = "Hello"

print(student) # {('a', 'b'): 'Hello'}

# ===================== 1. Unpacking ======================

bio = ("Mohammed", 10, "c")

name , std_class, div = bio
print(name) # "Mohammed"
print(std_class) # 10
print(div) # "C"

# *
fruits = ("banana", "apple", "cherry")

yellow, *others = fruits
print(yellow) # banana
print(others) # ['apple', 'cherry']