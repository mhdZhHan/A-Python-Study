# Scopes

# ================== 1. global scope  ================
a = 10 

def my_func():
    print(a)

my_func()
print(a)

# =================== 2. local scope ==================

def new_func():
    b = 200
    print(b)

new_func()
# print(b) # 'b' is not defined