# Q1 Wite a program that take salary as input. Using conditional statements, calculate the final tax rate based on the following criteria:# - If salary is less than 30,000, tax rate is 5%
# - If salary is between 30,000 and 70,000, tax rate is 15%
# - If salary is above 70,000, tax rate is 30%

salary = int(input("Provide you Salary to know tax rate: "))

if (salary < 30000):
    print("5% Tax Rate Applicable")
elif (salary > 30000 and salary < 70000):
    print("15% Tax Rate Applicable")
elif(salary > 70000):
    print("30% Tax Rate Applicable")        



# Q2 Write a function that takes two integers a and b and prints all even numbers between a and b (inclusive).
def print_even(a,b):
    for i in range(a,b+1):
        if(i %2 ==0):
            print(i)
   
print_even(1, 100)


# Q3 Write a function that prints a digits of a number, n, one by one. For example, if n is 12345, the output should be: Digits: 1 Digits: 2 Digits: 3 Digits: 4 Digits: 5

def print_number_digit(user_input):
    tostr = str(user_input)
    for digit in tostr:
        print("Digits:", digit)

print_number_digit(12345)


# Q4 Write a function to return the count the number of digits in a number. For example, if the input is 12345, the output should be: Number of digits: 5

def count_digits_in_number(number):
    toStr  = str(number)
    count =0
    for digit in toStr:
        count+=1
    print(count)  


# Q5 Write the function to return the sum of digitsof a number, n. For example, if n is 12345, the output should be: Sum of digits: 15


def print_sum_of_all_digit(number):
    toStr = str(number)
    totalValue = 0
    for digit in toStr:
        tonum= int(digit)
        totalValue +=tonum
    print(totalValue)

print_sum_of_all_digit(1234567890)


# Q6 Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.

def print_multiple_of_given_value(a,b):
    for number in range(a, b+1):
        if(number % 3 ==0 or number %5 ==0):
            print(number)

print_multiple_of_given_value(1,100)       


# Q7 Design a program that continuously input a number 'n'  from user and print if it is positive or negative until user enters "Quit" to stop the program.


user_input = input("Enter any number: ")
while user_input != "Quit":
    toNumber = int(user_input)
    if (toNumber>=0):
        print("Positive")
    elif(toNumber<0):
        print("Negative")
    else:
        print("put any valid number")  
    user_input = input("Enter any number: ")  


# Q8 Letʼs create a Simple that performs arithmetic operations. Create a function Calculator(a, b, operation) that performs addition, subtraction, multiplication, or division based on the operation parameter. [operation parameter can be '+', '-', '*', '/'].


def Calculator(a , b , operation):
    if(operation == '+'):
        output = a+b
        return output
    elif(operation == '-'):
        output = a-b
        return output
    elif(operation == "*"):
        output = a*b
        return  output  
    elif(operation == '/'):
        output = a/b
        return output
    else:
        print("Please Provide Valid Operation")      

output_value = Calculator(1,1,'+')
print(output_value)    


# Q9 Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.

def is_prime(number):
    if(number<=1):
        return False
    if(number>=2):
        count =0
        for i in range(2, number):
            if(number%i ==0):
                count+=1
            if(count==0):
                return True
            else:
                return False       
output = is_prime(101)
print(output)


# Q10 Letʼs create a Number Guessing Game. Given a secret number (already decided by you), write a program that ask the user to guess it and prints :
# • "Too high": if the guess is above the number
# • "Too low": if the guess is below 
# • "Correct!": if the guess matches 

user_input = int(input("Enter Any Number: "))
secret_number = 10
while user_input != secret_number:
    if(user_input<secret_number):
        print("Too Low!")
        user_input = int(input("Enter Any Number: "))
    elif(user_input>secret_number):
        print("Too High!")
        user_input = int(input("Enter Any Number: "))
    elif(user_input==secret_number):
        print("Correct!")
        break   


