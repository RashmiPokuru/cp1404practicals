"""
CP1404/CP5632 - Prac_03
Exceptions To Complete
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))

    except:
        print("Please enter a valid integer.")
print("Valid result is:", result)
