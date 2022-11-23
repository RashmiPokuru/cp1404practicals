"""
CP1404/CP5632 Practical 09
Taxi simulator program
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU_STRING = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator to use taxi."""
    print("Let's drive!")
    print(MENU_STRING)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            choose()
        elif choice == "D":
            drive()
        else:
            print("Invalid option")
        choice = input(">>>").upper()


main()
