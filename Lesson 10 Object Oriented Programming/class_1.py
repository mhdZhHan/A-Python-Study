# Class

class Student:
    first_name = "Mohammed"
    last_name = "Shajahan"
    student_class = 10
    division = "C"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

student1 = Student()
print(student1.student_class)
print(student1.division)
print(student1.full_name())
