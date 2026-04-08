#FILES OPERATIONS

#Read Mode:
f = open("sample.txt", "r")

#Whole File Read:
# data = f.read()
# print(data)
# print(type(data))

#Reads Line By Line:
data1 = f.readline()
print(data1)

data2 = f.readline()
print(data2)

f.close()

# Write Mode:
f = open("sample.txt", "w")

#Write Method Will Overwrite In The File:
f.write("This Will Overwrite \nThe text In Sample.txt File")

f.close()


# Append Mode:
f = open("sample.txt", "a")

f.write("\nThis Text Will Appended\nIn sample.txt File")

f.close()

# x Mode for Creating New Files And Write In The File:

f = open("sample2.txt", "x")

f.write("This Is The New txt File.")

f.close()

# Text Mode:
# We Can Read , Write Data In Text Mode By Default. But We Can Read , Write Data In Binary Mode Also By Using This Type Of Mode - "rb", "wb".

# + Mode - Opens Disk Files For Update (R/W):

# 1. r+ - Opens File For Reading And Writing. The File Pointer Is At The Beginning Of The File.
f = open("sample.txt", "r+")

f.write("123")
print(f.read())
f.close()

# 2. w+ - Opens File For Writing And Reading. Overwrites The Existing File If The File Exists. If The File Does Not Exist, Creates A New File For Reading And Writing.

f = open("sample.txt", "w+")

f.write("Hello World")
print(f.read())
f.close()


# 3. a+ - Opens File For Appending And Reading. The File Pointer Is At The End Of The File If The File Exists. That Is, The File Is In The Append Mode. If The File Does Not Exist, Creates A New File For Reading And Writing.

f = open("sample.txt", "a+")

f.write("123")
print(f.read())

f.close()


# Simple way to handle file operations using 'with' statement because it automatically takes care of closing the file after its suite finishes, even if an exception is raised.

with open("sample.txt", "r") as f:
    data = f.read()
    print(len(data))


# Deleting A File:
import os

os.remove("sample2.txt")


#Practice Problem:
# Write A Program To Find How Many Times The Word "Python" Occurs In A File.
data = True
count = 1
with open("sample.txt","r") as f:
    while data:
        data = f.readline()
        print(data)
        if("python" in data):
            print(f"Found Python at line {count}")
        count += 1


Exception Handling:

x = int(input("Enter Any Number: "))
ans = 10/x
print(ans)

try:
    x = int(input("Enter Any Number: "))
    ans = 10/x
except ZeroDivisionError:
    print("Division Is Not Allowed with zero")
except ValueError:
    print("Please Provide Integers")    
else:
    print(ans)
finally:
    print("Python Program Executed")    


# List Comprehensions:
# [Output for item in iterable if condition]
squares = []

for i in range(6):
    squares.append(i*i)

print(squares)

sq = [i*i for i in range(6) if i%2 !=0]
print(sq)

Num = [-2, -1, 0, 1, 2, 5]

Num = [0 if val < 0 else val for val in Num]

print(Num)

abc = ["hello", "python", 'language']

abc = [val.upper() for val in abc]
print(abc)


# Json Module:

import json
json_str ='{"name": "Hitesh","isEmployee": true}'
py_obj = json.loads(json_str)
print(type(py_obj),py_obj)


import json
py_obj = {
    "name": "Hitesh",
    "isEmployee": True
}
json_str = json.dumps(py_obj)
print(type(json_str),json_str)

import json
with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)

import json
py_obj = {
    "name":"Hitesh",
    "isEmployee": True
}

with open("data.json", "w")as f:
    json.dump(py_obj,f, indent =4 , sort_keys = True )
