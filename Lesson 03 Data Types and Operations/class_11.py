# String Formating

my_name = "Mohammed"
my_class = 10
my_age = 15

# ====================== 1. %-formatting ====================

print("Hai I'am %s" %my_name) # "Hai I'am Mohammed"
print("My name is %s. Iam studing in %s." %(my_name, my_class)) # "My name is Mohammed. Iam studing in 10"

# ====================== 1. .format() =======================

my_detail = "My name is {}. Iam studing in {}.".format(my_name, my_class)
print(my_detail) # "My name is Mohammed. Iam studing in 10"

# reference variables in any order by referencing their index
new_detail = "Class: {1} Name: {0} Age: {1}".format(my_name, my_class, my_age)
print(new_detail) # "Class: 10 Name: Mohammed Age: 1"

# ====================== 1. f-Strings =======================

print(f"Hello I'am {my_name}. Iam studing in {my_class}") # "Hello I'am Mohammed. Iam studing in 10"

# It would also be valid to use a capital letter F
print(F"Hello I'am {my_name}. Iam studing in {my_class}") # "Hello I'am Mohammed. Iam studing in 10"