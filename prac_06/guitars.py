"""
CP1404/CP5632 Practical - Playing the guitars
"""
from prac_06.guitar import Guitar


def main():
    """Store user's guitars in list until they enter blank name and then display details"""
    guitars = []
    print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitar = Guitar(name, year, cost)
    #     guitars.append(guitar)
    #     print(f"{guitar} added.")
    #     name = input("Name:")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_display = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name}, worth $ {guitar.cost}{vintage_display}")


main()
