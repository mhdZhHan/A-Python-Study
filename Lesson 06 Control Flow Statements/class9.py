# Loop Control Statement Continue

pets = ["dog", "cat", "parrot"]

for pet in pets:
    if pet == "cat":
        continue
    print(pet)

number = 0
while number < 10:
    if number == 5:
        continue
    print(number)
    number += 1