# Conditional Statements in Python
# Traffic Light System using if-elif-else
color = input("Enter Color: ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Look")
elif color == "green":
    print("Go")
else:
    print("Light Broken!")        


# Age Category Determination
age = int(input("Enter Your Age: "))
if age<13:
    print("Child")
elif age>=13 and age<18:
    print("Teenager")
else:
    print("Adult")       


# User Authentication System
username = input("Enter Username: ")
if (username =="Hitesh"):
    password = input("Enter Password: ")
    print("Checking for Password")
    if(password == "12345"):
        print("User Logged In")
    else:
        print("Incorrect Password!")    
else:
    print("Incorrect Username!")


# Divisibility Check
number = int(input("Enter Any Number: "))
if (number%5==0):
    print("True")
else:
    print("False")    


# Even or Odd Number Check
number = int(input("Enter Any number: "))
if(number % 2 == 0):
    print("Even")
else:
    print("Odd")    
    
