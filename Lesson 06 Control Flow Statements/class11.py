# Operations with Dictionary

student = {
    "name": "Mohammed",
    "class": 10,
    "division": "c"
}

# =============== 1. keys() ===============
print("============== 1. keys() ===============")

# for data in student:
#     print(data)

for data in student.keys():
    print(data)

# for data in student.keys():
#     print(student[data])

# =============== 2. values() ================
print("=============== 2. values() ================")

for data in student.values():
    print(data)

# ================ 3. item() ==================
print("================ 3. item() ==================")

for key,value in student.items():
    print(key,":",value)