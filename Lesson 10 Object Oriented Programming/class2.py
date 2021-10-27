# Class Instances

class Student:
    def __init__(self, first_name, last_name, class_, division):
        self.first_name = first_name
        self.last_name = last_name
        self.class_ = class_
        self.division = division

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


student1 = Student("Mohammed", "Shajahan", 10, "C")
student2 = Student("Ali", "A", 9, "B")
print(student1.full_name())
print(student2.full_name())
