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

