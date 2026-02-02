# Q1 Write a program to take User name and age as input and print it.
user_name = input("Please Enter your name: ")
user_age = input("Please Enter you age: ")
print("Welcome", user_name,",", "You are", user_age, "Years old!")


# Q2 Take a two numbers as input and print their Sum, Difference, Product and Quotient.
val1 = float(input("Enter 1st val: "))
val2 = float(input("Enter 2nd val: "))

print(val1+val2, "Sum")
print(val1-val2, "Diffrence")
print(val1*val2, "Product")
print(val1/val2, "Quotient")


# Q3 Ask the user to enter 3 numbers (2 integers and 1 float) and convert them to float and print their average.
val1 = float(input("Enter 1st value as Integer: "))
val2 = float(input("Enter 2nd value as Integer: "))
val3 = float(input("Enter 3rd value as float: "))

print((val1+val2+val3)/3)


# Q4 The user will input a value, convert it into integer, float and string and print the value and its type.
user_input = input("Enter any number: ")
integer_val = int(user_input)
float_val = float(user_input)
string_val = str(user_input)
print("Integer",integer_val, type(integer_val))
print("Float",float_val, type(float_val))
print("String",string_val, type(string_val))

# Q5 Evaluate the following expression and print the value:
x = 10 + 3 *2 **2
print(x)


# Q6 Write a program to swap the value of two numbers entered by the user.
val1 = float(input("Enter val1: "))
val2 = float(input("Enter val2: "))
print(val1)
print(val2)
val =val1
val1 = val2
val2 =val
print(val1)
print(val2)


# Q7 Ask the user for temperature in celcius. convert it to float and print the temperature in fahrenheit.
temp_clecius = float(input("Enter Temp in Celcius:"))
temp_fahrenheit = (temp_clecius*(9/5))+32
print("Temperature in fahrenheit: ", temp_fahrenheit)


# Q8 Take the radius as user input and print the area.
radius = float(input("Enter Radius: "))
PI = 3.14
area = PI *(radius **2)
print("Area of Radius", radius, "is", area)


# Q9 Ask the user for Principal, Rate and Time. convert them to float and calculate Simple Interest and print it.
principal =float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate: "))
time =float(input("Enter Time: "))
simple_interest =(principal*rate*time)/100
print("Simple Intrest:",simple_interest)


# Q10 Take a decimal number as input from the user and print its integer and fractional part.
float_number = float(input("Enter any decimal Value: "))
fractional_part = float_number%1.0
integer_part = float_number-fractional_part
print("Integer Value:",integer_part,"Fractional Value:",fractional_part)
