#Q1 Create a program that: 
# 1. Opens a file in write mode "names.txt", 
# 2. Writes 5 names (one per line) entered by the user, 
# 3. Then opens the same file in read mode and prints all names.

with open("names.txt", "w") as f:
    for i in range(6):
        name = input("Enter Name: ")
        f.write(name + "\n")

data = True      
with open("names.txt","r") as f:
    while data:
        data = f.readline()
        print(data)


#Q2 Opens a file in append mode "log.txt", and adds a new log entry (like "Program run successfully") then opens the file in read mode and prints all logs.   

with open("log.txt","a") as f:
    f.write("\nProgram run successfully")

with open("log.txt","r") as f:
    logs = f.read()
    print(logs)


#Q3. Create a Program that: 1. Has a list of numbers: [5, 10, 15, 20, 25] 2. Uses a list comprehension to create a new list with only numbers greater than 15 3. Prints the new list

num = [5, 10, 15, 20 ,25, 30]

num1 = [i for i in num if i > 15]
print(num1)