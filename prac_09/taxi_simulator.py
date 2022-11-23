"""
CP1404/CP5632 Practical 09
Taxi simulator program
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU_STRING = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator to use taxi."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU_STRING)
    option = input(">>>").upper()
    while option != "Q":
        if option == "C":
            current_taxi = choose(taxis)
        elif option == "D":
            pass
        else:
            print("Invalid option")
        option = input(">>>").upper()


def choose(taxis):
    """Choose taxi from list of available taxis."""
    display_available_taxis(taxis)
    pass


def display_available_taxis(taxis):
    """Display available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
        



main()
