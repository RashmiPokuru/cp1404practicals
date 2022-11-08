"""
CP1404/CP5632 Practical - Client code to use the Guitar class.
"""
from prac_06.guitar import Guitar

FILE_NAME = "guitars.csv"


def main():
    """Store guitars from file into list."""
    guitars = load_guitars(FILE_NAME)
    print(guitars)
    print("My new guitars!")
    add(guitars)
    guitars.sort()
    print(guitars)
    for guitar in guitars:
        print(guitar)
    save_file(guitars, FILE_NAME)


def add(guitars):
    """Add new guitars."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(guitars)
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")


def load_guitars(file_name):
    """Load guitars from file"""
    guitars = []
    with open(file_name, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def save_file(guitars, file_name):
    print(guitars)
    with open(file_name, 'w') as out_file:
        for guitar in guitars:
            print(guitar.name, guitar.year, guitar.cost, sep=',', file=out_file)



main()
