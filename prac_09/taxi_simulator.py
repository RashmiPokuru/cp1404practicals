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
    option = input(">>> ").upper()
    while option != "Q":
        if option == "C":
            print("Taxis available: ")
            display_available_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif option == "D":
            if current_taxi:
                current_taxi.start_fare()
                distance = get_non_negative_number()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you {trip_cost:.2f}")
                bill_to_date += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU_STRING)
        option = input(">>> ").upper()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_available_taxis(taxis)


def display_available_taxis(taxis):
    """Display available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_non_negative_number():
    """Get non-negative number"""
    try:
        number = int(input("Drive how far? "))
        if number < 0:
            print("Invalid number")
        else:
            return number
    except ValueError:
        print("Invalid number")


main()
