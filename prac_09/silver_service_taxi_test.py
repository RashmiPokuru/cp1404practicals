"""
CP1404/CP5632 Practical 09
Program to test SilverServiceTaxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class"""
    silver_service_taxi = SilverServiceTaxi("Silver Taxi", 150, 2)
    silver_service_taxi.drive(18)
    print(f"{silver_service_taxi} : Trip fare is ${silver_service_taxi.get_fare():.2f}")


main()
