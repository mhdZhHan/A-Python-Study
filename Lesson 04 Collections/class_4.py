# List Operations Removing Elements

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# =================== 1. remove() ================

# removing list element
x.remove(10)

print(x)

# ================== 2. del ======================

# removing list element using index
del x[2]

print(x)

# ================== 2. pop() =====================

y = [1, 2, 3, 4, 5, 6, 7]

# remove last element in a list
y.pop()
print(y)

# store popped element
z = y.pop()
print(z)

# passing index in pop
a = y.pop(1)
print(y)