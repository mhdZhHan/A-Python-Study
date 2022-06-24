# Random Module
import random


x = random.random()
print(x)

# return a random flot number in 1 to 100
print(random.uniform(1, 100))

# return a random int number in 1 to 100
print(random.randint(1, 100))

letters = ["a", "b", "c", "d"]
# return random items in a list
print(random.choice(letters))

print(random.randrange(1, 100, 5))

numbers = [1, 2, 33, 45, 4, 5, 6, 78, 66, 100]
# shuffling a list
print(random.shuffle(numbers))

print(random.sample(numbers, 3))