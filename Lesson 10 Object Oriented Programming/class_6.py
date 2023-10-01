# Method Overriding => super()

class Animal:
    def __init__(self, name):
        self.name = name

    def activity(self):
        return f'{self.name} is running...'


# __init__ overriding
class Cat(Animal):
    def __init__(self, bread):
        self.bread = bread
        super().__init__("Kitty")

    def activity(self):
        return f'{self.bread} cat is drinking milk🍼🍼🍼'

cat = Cat("bobtail")
print("The cat name is",cat.name)
print(cat.activity())

print('\n')

dog = Animal("lobby")
print("The dog name is",dog.name)
print(dog.activity())
