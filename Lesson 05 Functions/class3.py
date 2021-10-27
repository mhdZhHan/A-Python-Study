# Arguments

# ============= 1. Positional Argument ==========

def add(x, y):
    return x + y

z = add(100, 50)
print(z) # 150

# ============= 2. Keyword Argument =============

def sub(x, y):
    return x - y

z = sub(y=200, x=300)
print(z) # 100