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

