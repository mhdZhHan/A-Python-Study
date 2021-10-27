# Tuple Operations

x = (1, 2, 3, 1)
y = (4, 5, 6)

print(x + y) # (1, 2, 3, 1, 4, 5, 6)

print(x * 3) # (1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1)

print(x.index(3)) # 2
print(x.count(1)) # 2
print(1 in x) # True