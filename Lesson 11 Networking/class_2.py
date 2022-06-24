# JSON
import json


my_json = '''{
    "students": [
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
        }
    ]
}'''

# print(my_json)
print(type(my_json)) # <class 'str'>
# ============== 1. json.loads() ==================

converted_dict = json.loads(my_json)
# print(converted_dict)
print(type(converted_dict)) # <class 'dict'>


# ============== 2. json.load() ===================

with open("student.json", "r") as json_file:
    new_dict = json.load(json_file)

print(new_dict)
print(type(new_dict)) # <class 'dict'>

'''
# 🗒Note
# ⚠️⚠️ if you get "FileNotFoundError: [Errno 2] No such file or directory: 'student.json'" error
# first we will run class1.py in this directory and after run this file
'''