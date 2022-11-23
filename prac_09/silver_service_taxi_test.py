"""
CP1404/CP5632 Practical 09
Program to test SilverServiceTaxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class"""
    silver_service_taxi = SilverServiceTaxi("Silver Taxi", 150, 2)
    silver_service_taxi.drive(18)
    print(silver_service_taxi)
    print(silver_service_taxi.get_fare())


main()
