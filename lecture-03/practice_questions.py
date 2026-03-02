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