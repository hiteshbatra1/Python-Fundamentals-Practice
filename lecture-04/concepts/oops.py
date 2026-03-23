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


# INSTANCE METHODS, CLASS METHODS, STATIC METHODS
class Laptop:
    storage_type = "SSD"

    def __init__ (self,RAM,storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_info(cls): #CLASS METHOD
        print(f"The Laptop Storage Type is {cls.storage_type}")  

    def get_info(self):  #INSTANCE METHOD
        print(f"The Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}") 

    @staticmethod
    def get_dicounted_price (price, discount): #STATIC METHOD
        final_price = price - (discount * price / 100)
        print(f"The Final Price of Laptop is {final_price}")
           

Laptop1 = Laptop("16gb","512gb")
Laptop2 = Laptop("8gb", "256gb")

Laptop1.get_info()
Laptop2.get_info()
Laptop1.get_storage_info()
Laptop.get_storage_info()

Laptop1.get_dicounted_price(50000, 10)


#PRACTICE PROBLEM
class ProductStore:
    store_name = "store"
    count = 0
    def __init__ (self,name,price):
        self.name = name
        self.price = price
        ProductStore.count += 1

    def get_productinfo (self):
        info = f"Product Name: {self.name} And Price: {self.price}"
        return info

    @classmethod
    def get_totalproducts (cls):
        print(f"Total Products {cls.count}")    

    @staticmethod
    def get_discountedprice (price,discount):
        final_price =   price - (discount * price/100)
        print(f"The final Price is {final_price}")

prod1 = ProductStore("Phone", 10000)

info_product = prod1.get_productinfo()

print(info_product)
ProductStore.get_totalproducts()

prod1.get_discountedprice(prod1.price, 10)


#ENCAPSULATION AND DATA HIDING
class BankAccount:
    def __init__ (self, name, balance):
        self.name = name
        # self.balance = balance  PUBLIC ATTRIBUTE
        # self._balance = balance   PROTECTED ATTRIBUTE
        self.__balance = balance    #PPRIVATE ATTRIBUTE

    def get_balance (self):     #GETTER MEHTOD
        return self.__balance  

    def set_balance (self, newBalance): #SETTER METHOD
        self.__balance = newBalance


acc1 = BankAccount("Hitesh", "10m")
acc1.set_balance("200m")
print(acc1.name, acc1.get_balance())


# INHERITANCE

# 1. SINGLE LEVEL INHERITANCE
class Employee:
    start_time = "10AM"
    full_time = "6PM"

    def change_fulltime (self, new_fulltime):
        self.full_time = new_fulltime


class Teacher(Employee):
    def __init__ (self, subject):
        self.subject = subject
t1 = Teacher("English")
print(t1.subject, t1.start_time, t1.full_time)



class AdminStaff(Employee):
    def __init__ (self, role):
        self.role = role
staff1 = AdminStaff("Manager")
staff1.change_fulltime("7pm")
print(staff1.role, staff1.start_time, staff1.full_time)


# MULTI LEVEL INHERITANCE

class Employee:
    start_time = "10AM"
    full_time = "6PM"

class AdminStaff(Employee):
    def __init__ (self,role):
        self.role = role
        
class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

acc1 = Accountant(25000, "CA")
print(acc1.salary, acc1.role, acc1.start_time, acc1.full_time)


# MULTIPLE INHERITANCE

class Teacher:
    def __init__ (self, salary):
        self.salary = salary

class Student:
    def __init__ (self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__ (self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name         


ta1 = TA(25000, 10, "Hitesh")

print(ta1.salary, ta1.gpa, ta1.name)


# ABSTRACTION IN PYTHON

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound (self):
        pass

class Lion(Animal):
    def make_sound (self):
        print("ROAR!")


lion = Lion()

lion.make_sound()