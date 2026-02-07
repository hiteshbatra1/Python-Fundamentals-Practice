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
