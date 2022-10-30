"""
CP1404/CP5632 Practical - Playing the guitars
"""
from prac_06.guitar import Guitar


def main():
    """Store user's guitars in list until they enter blank name and then display details"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name:")


main()
