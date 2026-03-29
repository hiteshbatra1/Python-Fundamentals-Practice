#Q1 Create a BankAccount class with methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__ (self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    #METHOD TO DEPOSIT IN BANK ACCOUNT:
    def add_deposit (self, deposit_ammount):
        self.balance += deposit_ammount
        print(f"Total Balance Now: {self.balance}")

    #METHOD TO WITHDRAW FROM BANK ACCOUNT:
    def withdraw (self, withdraw_ammount):
        self.balance -= withdraw_ammount
        print(f"Total Balance Now: {self.balance}")

    #METHOD FOR CHECK BALANCE:
    def check_balance (self):
        print(f"The Current Balance Is RS.{self.balance}")

#INSTANCE OF BANKACCOUNT CLASS:
acc1 = BankAccount(12345, "Hitesh", 100000)

#DEPOSIT OF 100000:
acc1.add_deposit(100000)

#WITHDRAW OF 50000:
acc1.withdraw(50000)

#CHECK BALANCE:
acc1.check_balance()

print(acc1.account_number,acc1.owner_name,acc1.balance)


#Q2 Create a Class Book with attributes title, author, and year. Include a method to display book details.

class Book:
    reviews = []
    def __init__ (self,title,author):
        self.title = title
        self.author = author

    #Method To Add Review To A Book:
    def add_reviews (self, review):
         self.reviews.append(review)

    #Method To Count All Reviews To A Book
    def count_reviews (self):
        review_array = self.reviews
        review_count = len(review_array)
        print(f"Total Reviews To {self.title} Book By {self.author} are {review_count}")

    #Method To Display Reviews Of A Specific Book:
    def display_reviews (self):
        review_array = self.reviews
        for review in review_array:
            print(review)

#Instance Of Book Class:       
B1 = Book("Hello World", "Hitesh")

# Adding Reviews To Specific Book:
B1.add_reviews("Very Good")
B1.add_reviews("Good")

# To Get Total Reviews On A Book:
B1.count_reviews()

# To Get Each Review Of Specific Book:
B1.display_reviews()

print(B1.title,B1.author,B1.reviews)


#Q3 Create a Student class with private attributes for name , roll number and marks. Provide getter and setter methods for each attribute with validation.

#  Student Class With Private Attributes And Getter-Setter Methods
class Student:
    def __init__ (self, name , roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

# Getter Methods 
    def get_name (self):
        print(f"Name is {self.__name}")

    def get_roll_no (self):
        print(f"Roll No. is {self.__roll_no}")    

    def get_marks (self):
        print(f"Marks is {self.__marks}")  

# Setter Methods
    def set_name (self , name):
        if(name == ""):
            print("Name Cannot Be Empty")
            return
        self.__name = name   

    def set_rollno (self, roll_no):
        if (roll_no < 1 or roll_no > 100):
            print("Please Provide Roll No. Between 1 To 100")
            return
        self.__roll_no = roll_no

    def set_marks (self, marks):
        if(marks < 0):
            print("Please Provide Valid Marks")    
            return
        self.__marks = marks

# Instance Of Student Class
stu1 = Student("Hitesh", 1, 100 )

# Using Setter Methods To Set Values With Validation
stu1.set_name("Hitesh")
stu1.set_rollno(100)
stu1.set_marks(100)

# Using Getter Methods To Get Values
stu1.get_name()
stu1.get_roll_no()
stu1.get_marks()
