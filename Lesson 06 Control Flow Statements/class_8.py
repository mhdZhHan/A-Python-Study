# Loop Control Statement Break

pets = ["cat", "parrot", "dog"]

for pet in pets:
    # print(pet)
    if pet == "parrot":
        break
    print(pet)


number = 0
while number < 10:
    print(number)
    if number == 5:
        break
    number += 1