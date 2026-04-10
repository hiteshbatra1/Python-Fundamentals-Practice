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