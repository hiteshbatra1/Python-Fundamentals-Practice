word = "Python"
print(len(word))

# Concatenate
word1 = "I Love"
word2 = "Python"
sentence = word1 + " " + word2
print(sentence)

word = "Python"
for ch in word:
    print(ch)

# For accessing any index in String
print(word[2])

Slicing in String
print(word[2:4])
print(word[:len(word)])
print(word[0:])
print(word[-4:-2])


# String Formatting / Dynamic Strings
# 1. Format Method

a = 1
b = 1
sum = a+b

# Normal Formatting
print("The Sum Of {} and {} is {}".format(a,b,sum))

# Index Based Formatting
print("The Sum Of {0} and {1} is {2}".format(a,b,sum))

# Value Based Formatting
print("The Value Of Variables is {a} and {b}".format(a=5,b=10))


# 2. F-Strings Literal String Interpolation
print(f"The Sum Of {a} and {b} is {a+b}")


# Data Types In Python
# 1. Lists

marks = [90, 80, 70 ,80,100]
print(marks[0])
print(len(marks))
print(len(marks)-1)
print(marks[len(marks)-1])

marks[2] = 90
print(marks[2])

# Slicing In Lists
print(marks[:3])
print(marks[1:])

# Methods In Pyhton
# 1. Append
marks.append(90)
print(marks)

# 2. Insert
marks.insert(2, 90)
print(marks)

# 3. Sort
numbers = [2,3,5,4,1,6,8,9,7,0,10]
numbers.sort()
print(numbers)

numbers.sort(reverse= True)
print(numbers)


# 4.Reverse

numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)

# Loops In List
numbers = [1,2,3,4,5,6,7,8,9,10]
for val in numbers:
    print(val)


# This Search In List We Did Is Linear Search
numbers = [1,2,3,4,5,6,7,8,9,10]
i =0
for val in numbers:
    if(val == 5):
        print(f"The Value {val} is at Index {i}")
    i+=1


# 2. Tuples
tup = (1,2,3,4,5)
print(tup[1])
print(type(tup))
print(len(tup))
print(tup[1:])

for val in tup:
    print(val)


sum = 0
for val in tup:
    sum += val
print(sum)    


# Methods Of Tuples
1. Return 1st Occurence Index
tup = (1,2,3,4,5,1,2,)
print(tup.index(1))

# 2. Return Total Occurence Count
tup = (1,2,3,4,5,1,2,1,2,1,2,1,2,1)
print(tup.count(1))


# 3. Dictonary
info = {
    "name": "Hitesh",
    "Marks": 100,
    "Subjects":["Math","Science", "English"],
}
print(info)
print(type(info))

print(info["name"])

info["name"] =  "Hitesh Batra"
print(info["name"])

# Methods In Tuples
# 1. To Get All Keys From Dictonary

dict_keys = list(info.keys())
print(dict_keys)

# 2. To Get All Values From Dictonary
dict_values = list(info.values())
print(dict_values)

# 3. To Get {Key:Value} From Dictonary
dict_items = dict(info.items())
print(type(dict_items))
print(dict_items)

# 4. To Get Value According To Key From Dictonary
dict_get = info.get("name")
print(dict_get)

# 5. To Add New Item To Dictonary
info.update({"city":"Hisar"})
print(info)


# 4. Sets
sets = {1,2,3,4,5,6,6,6,7,7,8,8,9,9,0,0,2,3,2,10}
print(sets)
print(type(sets))

sets.add(11)
print(sets)

empty_set = set()
print(type(empty_set))

# Methods Of Set
# 1. Add Value In Set
sets.add(100)
print(sets)

# 2. Remove Value In Set
sets.remove(0)
print(sets)

# 3. Empties The Set
sets.clear()
print(sets)

# 4. Removes Random Value
sets.pop()
print(sets)

# 5. Union Method In Set
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

union_set = set1.union(set2)
print(union_set)

# 6. Intersection Method In Set
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

intersection_set = set1.intersection(set2)
print(intersection_set)


# PRACTICE QUESTION:

info = [
    ("Alice","Maths"),
    ("Bob", "Science"),
    ("Alice","Science"),
    ("Charlie","Maths"),
    ("Bob","Maths"),
    ("Alice","English"),
    ("Charlie","English")
]

# 1. Lists All Unique Courses
subject = []
for tup in info:
    subject.append(tup[1])
unique_subjects = set(subject)    
print(f"The Unique Subjects Are {unique_subjects}") 


# 2. Lists Students Enrolled In English
check_student_details = input("Enter Course Name To Know Enrolled Students Details:")
student_enrolled_in_english= {}
for name,course in info:
    if(course== check_student_details):
        student_enrolled_in_english.update({
            name:course
        })

print(student_enrolled_in_english)



# 3. Create Dictionary (Student, Set Of Courses)
dict_info = {}
for name, course in info:
    if(dict_info.get(name) == None):
        dict_info.update({
            name: set()
        })
        dict_info.get(name).add(course)
    else:
        dict_info.get(name).add(course)

print(dict_info)

