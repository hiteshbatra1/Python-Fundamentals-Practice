# OOPS - OBJECT ORIENTED PROGRAMMING IN PYTHON

class Student:
    subject = "Python"
    marks = 100

stu1 = Student()
stu2 = Student()

print(stu1)
print(stu2)
print(stu1.subject)


# Constructor Concept
class Student:
    def __init__ (self, name):
        self.name = name
    subject = "Python"

stu1 = Student("Hitesh")

print(stu1.name)

class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks

    def get_marks (self):
        return self.marks   

stu1 = Student("Hitesh", 100)

print(stu1.name)
print(stu1.get_marks())


# CLASS ATTRIBUTE AND INSTANCE ATTRIBUTE
class Student:
    college = "ABC College"

    def __init__ (self,name,gpa):
        self.name = name
        self.gpa = gpa

stu1 = Student("Hitesh", 10)

print(stu1.name,stu1.gpa, Student.college)
