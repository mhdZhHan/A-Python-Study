# Default Arguments

def add(x, y, z=100):
    return x + y + z

print(add(10, 20)) # 130

print(add(20, 30, 10)) # 60

print(add(z=20, y=5, x=10)) # 35

print(add(10, 10, z=1)) # 21