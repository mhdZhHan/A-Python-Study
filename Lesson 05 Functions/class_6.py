# Kwargs

def add(x, y=10, **Kwargs):
    print(type(Kwargs))
    print(Kwargs)
    print("Age:", Kwargs["age"])
    return x + y

z = add(10, y=30, name="Mohammed", age=15)
print(z)