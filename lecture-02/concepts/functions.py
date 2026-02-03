# functions in python
def hello():
    print("Hello")
hello()    


# function with parameters and return value
def sum(a , b):
    s = a + b
    return s


val = sum(5,5)    
print(val)


# function to calculate average of three numbers
def avg(a,b,c):
    sum = a+b+c
    a = sum/3
    return a

val = avg(5,10,15)   
print(val)


# lambda function
sum = lambda a,b:a+b
print(sum(5,5))

def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    return fact

output = factorial(5)
print(output)

    
    

