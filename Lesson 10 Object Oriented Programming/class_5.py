# Method Overriding

class Animal:
    def __init__(self, name):
        self.name = name

    def activity(self):
        return f'{self.name} is running...'


# method overriding
class Cat(Animal):
    def activity(self):
        return f'{self.name} is drinking milk🍼🍼🍼'

cat = Cat("Kitty")
print(cat.activity())

dog = Animal("lobby")
print(dog.activity())
