"""
CP1404/CP5632 Practical - Client code to use the Guitar class.
"""
from prac_06.guitar import Guitar
import csv

FILE_NAME = "guitars.csv"


def main():
    """Store guitars from file into list."""
    guitars = load_guitars(FILE_NAME)
    for guitar in guitars:
        print(guitar)


def load_guitars(file_name):
    guitars = []
    with open(file_name, 'r') as in_file:
        guitars.append(csv.reader(in_file))
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars

main()

