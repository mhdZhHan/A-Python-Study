# Dictionary Operations Removing items

student = {
    "name": "Mohammed",
    "class": 1,
    "division": "c",
    "subjects": ["Python", "Java", "JavaScrip"]
}

# =================== 1. pop() =====================

x = student.pop("subjects", "default")
y = student.pop("marks", "default")

print(student)
print(x)
print(y) # default

# =================== 1. popitem =====================

# remove last item in dictionary
student.popitem()
print(student)

# =================== 1. del =====================

del student["name"]
print(student)

# remove entire dictionary

del student
# print(student) # 'student' is not defined

# =================== 1. clear() =====================

lang = {
    'name': 'python',
    'version': '3.9.0',
}
print(lang)

# clear the dictionary
lang.clear()
print(lang) # {}

