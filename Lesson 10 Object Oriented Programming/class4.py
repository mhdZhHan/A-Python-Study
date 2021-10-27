# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def running(self):
        return f'{self.name} is running...'


# 'Cat' class inherit 'Animal' class properties and methods
class Cat(Animal):
    pass

cat = Cat("Kitty")

print(cat.name)
print(cat.running())
