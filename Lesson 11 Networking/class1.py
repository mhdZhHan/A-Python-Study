# JSON
import json


students_dict = {
    "students" : [
        {
            "name": "Mohammed",
            "class_": 10,
            "division": "C"
        },
        {
            "name": "Ali",
            "class_": 9,
            "division": "A"
        },
        {
            "name": "Osman",
            "class_": 10,
            "division": "D"
        },
    ]
}

print(type(students_dict)) # <class 'dict'>
# print(students_dict)

# =============== 1. json.dumps() =================

json_string = json.dumps(students_dict, indent=4)
print(type(json_string)) # <class 'str'>
print(json_string)

# =============== 2. json.dump() ===================

with open("./student.json", "w") as json_file:
    json.dump(students_dict, json_file)