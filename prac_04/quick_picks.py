"""
CP1404/CP5632 Prac 4 - Lists
"Quick Pick" Lottery Ticket Generator
"""
from random import randint

NUMBER_OF_COLUMNS = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    line_numbers = [randint(MINIMUM_NUMBER, MAXIMUM_NUMBER) for j in range(NUMBER_OF_COLUMNS)]
    line_strings = [f"{number:2}" for number in line_numbers]
    print(line_numbers)
    print(line_strings)

