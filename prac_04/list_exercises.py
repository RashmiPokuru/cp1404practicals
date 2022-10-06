"""
CP1404/CP5632 Prac_04 - Lists
Intermediate Exercises
"""
# Basic list operations
# Print details of a list of numbers
NUMBER_OF_NUMBERS = 5
numbers = []
for i in range(NUMBER_OF_NUMBERS):
    number = int(input(f"Number: "))
    numbers.append(number)
# print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# Woefully inadequate security checker
# Check if the user is in the list of authorised users and print access result
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your username: ")
# username = "Jimbo" #should print Access denied
# username = "Inter" #should print Access denied
# username = "jimbo" #should print Access granted
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
