# Args

def add(x, y, *args):
    print(args)
    print(type(args)) #<class 'tuple'>
    return x + y


print(add(10, 5, 30, 50, 50)) # 15