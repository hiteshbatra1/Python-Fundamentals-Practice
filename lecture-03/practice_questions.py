# Q1 Ask the user for a string and check whether it is a palindrome or not.

user_input = input("Enter Any Word To Check Whether Its Palindrome Or Not: ")
user_input_reverse_copy = user_input[::-1]

if(user_input == user_input_reverse_copy):
    print(f"Yes {user_input} Is An Palindrome")
else:
    print(f"No {user_input} Is Not An Palindrome. Please Try Again With Diffrent Word")
