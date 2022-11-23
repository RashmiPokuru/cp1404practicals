"""
CP1404/CP5632 Practical 09
Taxi simulator program
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU_STRING = "q)uit, c)hoose taxi, d)rive"
MINIMUM_NUMBER = 0


def main():
    """Taxi simulator to use taxi."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
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
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU_STRING)
        option = input(">>>").upper()


def choose(taxis):
    """Choose taxi from list of available taxis."""
    display_available_taxis(taxis)
    taxi_choice = get_valid_number(MINIMUM_NUMBER, len(taxis))


def display_available_taxis(taxis):
    """Display available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_number(minimum_number, maximum_number):
    """Get valid number in the range."""
    try:
        number = int(input(">>> "))
        if number < minimum_number or number > maximum_number:
            print("Invalid taxi choice")
        else:
            is_valid_number = True
            return number
    except ValueError:
        print("Invalid taxi choice")


main()
