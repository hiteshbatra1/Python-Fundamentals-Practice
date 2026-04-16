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




#Q4 Create a Python dictionary of 3 cities and their populations. Save it to "cities.json". 1. Then load the JSON and print each city and its population. 2. Ask the user for a new city & its population - update this info in the json file
import json
city_info = {
    "Delhi": "30m",
    "Hyderbad": "10m",
    "Banglore":"20"
}

with open("cities.json", "w") as f:
    json.dump(city_info, f, indent = 4)

with open("cities.json","r") as f:
    data = json.load(f)
    for city,population in data.items():
        print(f"City:{city} Population:{population}")

new_city = input("Enter City Name: ")
new_population = input("Enter Population Size:")
data[new_city] = new_population

with open("cities.json", "w") as f:
    json.dump(data,f,indent=4)
    print(f"New city:{new_city} with Population of {new_population} added")


# Q5 Write a program that tries to open in read mode. If the file does not exist, catch the exception and print "File not found!"

try:
    with open("file.txt", "r") as f:
        data = f.read()
except:
    print("File Not Found")
else:
    print(data)    


