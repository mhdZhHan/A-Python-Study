# Class vs Instance

class Student:
    language = "Malayalam"
    def __init__(self, name, class_, division):
        self.name = name
        self.class_ = class_
        self.division = division


student1 = Student("Mohammed", 10, "C")
student2 = Student("Ali", 10, "C")

print(Student.language)
print(student1.language)

student2.language = "Arabic"
print(student2.language)