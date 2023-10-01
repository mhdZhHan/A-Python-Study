# List Operations - Insert and find items

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ================== 1. insert() ====================

x.insert(2, 1)

x.insert(len(x), 11)

x.insert(0, 100)

print(x)

# ====================== 2. Find Items ================

y = ["Apple", "Orange", "Grapes", "Banana", "Watermelon", "Apple"]

print("Apple" in y) # True

print("Pineapple" in y) # False

print("Pineapple" not in y) # True

print(y.count("Apple")) # 2

# =================== 3. index() =========================

z = [1, 2, 3, 4, 5, "Grapes", "Banana", "Watermelon", "Apple"]

# show index of a element
print(z.index(3)) # 2
print(z.index("Apple")) # 8

#  show index of a element in a particular position

a = [1, 2, 3, 4, 5, 6, 1, 7, 8, 9, 10, 1, 2, 1]

print(a.index(1,5,10)) # 6

print(a.index(1,8)) # 11