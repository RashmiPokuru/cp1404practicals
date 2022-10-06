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
    row_numbers = [randint(MINIMUM_NUMBER, MAXIMUM_NUMBER) for j in range(NUMBER_OF_COLUMNS)]
    print(row_numbers)
