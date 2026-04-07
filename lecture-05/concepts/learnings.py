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

