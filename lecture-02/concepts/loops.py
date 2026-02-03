# While Loop Example
i = 1
while (i <= 5):
    print("Hello World!")
    i +=1
print("Value of I=",i)    

i = 1

# Print numbers from 1 to 5
while (i<=5):
    print(i)
    i+=1


# Print numbers from 5 to 1
i = 5
while (i>=1):
    print(i)
    i-=1


# Print multiplication table of a number
n = int(input("Enter any Number: "))
i = 1
while (i<=10):
    print(n*i)
    i+=1


# Print sum of first n natural numbers
i = 1
while (i<=10):
    if(i % 6 ==0):
        break
    print(i)
    i+=1

# Print numbers from 1 to 10 except multiples of 6
i = 1
while(i<=10):
    if(i%6==0):
        i+=1
        continue
    print(i)
    i+=1


# Print odd numbers from 1 to 10
i = 1
while(i<=10):
    if(i%2!=0):
        print(i)
    i+=1    


# Print odd numbers from 1 to 10 using continue
i = 1
while(i<=10):
    if(i%2 ==0):
        i+=1
        continue
    print(i)
    i+=1    


# For Loop Examples
string = "Hello"
for val in string:
    print(val)


# Check if a character exists in a string
string = "Hello"
if "o" in string:
    print("o exists in string")


# Print numbers from 0 to 4
for i in range(5):
    print(i)


# Print "Hello world" 5 times using range
for i in range(5):
    print("Hello world")


# Count occurrences of 'i' in a string
word = "artificial intelligence"
count = 0
for val in word:
    if(val == "i"):
        count+=1
print(count)        

string = "artificial"
count = 0

for val in string:
    if(val == "a" or val == "e" or val ==  "i" or val == "o" or val == "u"):
        count+=1

print(count)       


# Different usages of range()
for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(0, 11 ,2):
    print(i)

number = int(input("Enter any number:"))
count =0

for val in range(1,number+1):
    print(val)
    count += val
print(count)    



