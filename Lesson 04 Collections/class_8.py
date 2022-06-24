# Dictionary Operations Adding and retreving data

student = {
    "name": "Mohammed",
    "class": 10,
    "division": "c",
}

dict2 = {"marks": [10, 20]}

# ========================== 1.update() ===============================

student.update(dict2)

student.update(sub=["Python", "Django"])

print(student)

# ========================== 2.Retreving ===============================

# print(student["X"]) # KeyError: 'X'

# ================ get() nmethod ====================

print(student.get("name", "default"))

print(student.get("x", "default"))