# Q1 Ask the user for a string and check whether it is a palindrome or not.

user_input = input("Enter Any Word To Check Whether Its Palindrome Or Not: ")
user_input_reverse_copy = user_input[::-1]

if(user_input == user_input_reverse_copy):
    print(f"Yes {user_input} Is An Palindrome")
else:
    print(f"No {user_input} Is Not An Palindrome. Please Try Again With Diffrent Word")


# Q2 Given a list of integers compute the average of all numbers in the list.

list_of_numbers = [10,20,30,40,50]
sum = 0
for val in list_of_numbers:
    sum += val

avg = sum/len(list_of_numbers)
print(avg)  



# Q3 Input two lists of integers from the user. Merge them in to one list and sort the result.

user_input1 = list(input("Enter The Numbers: "))
user_input2 = list(input("Enter The Numbers: "))
print(user_input1)
print(user_input2)
sort_list = user_input1[:]

for val in user_input2:
    sort_list.append(val)

print(sort_list)
sort_list.sort()

print(sort_list)


# Q4 Given a tuple of integers, create: 
# A tuple of all even numbers 
# A tuple of all odd numbers

tup = (1,2,3,4,5,6,7,8,9,10)
even_tup = []
odd_tup =[]


for val in tup:
    if(val %2 ==0):
        even_tup.append(val)
    else:
        odd_tup.append(val)


even_tup1 = tuple(even_tup)
odd_tup1 = tuple(odd_tup)

print(tup)
print(type(even_tup1))
print(even_tup1)
print(type(odd_tup1))
print(odd_tup1)


# Q5 Create a dictionary where: 
# Keys = student names 
# Values = marks(integer) 
# Write a menu-based program where user presses a key (ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ) depending on the operation they want toper form on the dictionary:
# 1. A-Add a student
# 2. B-Update marks 
# 3. C-Search for a student 
# 4. D-Display all students and marks

user_input = input("Enter Any Operation: ")
dict_info = {
    "hitesh":70
}

if(user_input == "A"):
    student_name = input("Enter The Name Of Student: ")
    marks = int(input("Enter Marks Of Student: "))
    dict_info.update({
        student_name: marks
    })
    print("Added New Student In Dictionary")
    print(dict_info)
elif(user_input == "B"):
    student_name = input("Enter The Name Of Student: ")
    update_marks = int(input("Enter Marks You Want To Update: "))
    dict_info[student_name]= update_marks
    (print(f"Updated The Marks of {student_name}"))
    print(dict_info)
elif(user_input == "C"):
    student_name = input("Enter Name Of The Student To Get Info: ") 
    student_marks = dict_info.get(student_name)  
    print(f"The Marks Of {student_name} is {student_marks}") 
elif(user_input == "D"):
    all_info = dict_info
    print(all_info)
else:
    print("Please Provide A Valid Input")


# Q6 Given a list of words: Create a dictionary that maps each word to its length.

list= ["apple", "banana","kiwi","cherry","mango"]
dict = {}
for val in list:
    if(dict.get(val) == None):
        dict.update({
            val: len(val)
        })
   
print(dict)


# Q7 Write a program that takes a string from the user and prints the number of spaces in the string.

user_input = input("Enter Any String: ")
count = 0
for val in user_input:
    if(val ==" "):
        count +=1
print(f"The Spaces In The String Is {count}")


# Q8 Write a program to check whether two lists share no common elements.

list_1 = [1,2,3,4,5]
list_2 = [4,5,6,7,8,9,10]

set_list1 = set(list_1)
set_list2 = set(list_2)

set_list_union = set_list1.union(set_list2)
list1 = list(set_list_union)
print(type(list1))
print(list1)

set_list_intersection = set_list1.intersection(set_list2)
list2 = list(set_list_intersection)
print(type(list2))
print(list2)


# Q9 Given a list, print all elements that appear more than once in the list.

list1 = [1,2,3,4,5,6,7,1,2]
seen = set()
duplicate = set()

for val in list1:
    if(val in seen):
        duplicate.add(val)
    else:
        seen.add(val)
print(duplicate)  