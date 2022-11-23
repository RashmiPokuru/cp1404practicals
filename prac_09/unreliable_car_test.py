"""
CP1404/CP5632 Practical 09
Program to test UnreliableCar class.
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test Unreliable Car class for various random numbers and distances."""
    # reliable_car should drive for all random numbers as reliability is maximum
    reliable_car = UnreliableCar("Reliable car", 150, 100)  # Car with maximum reliability = 100
    print(f"{reliable_car} drove {reliable_car.drive(80)} km")

    # unreliable_car should not drive for all random numbers as reliability is maximum
    unreliable_car = UnreliableCar("Unreliable car", 150, 0)  # Car with maximum reliability = 0
    print(f"{unreliable_car} drove {unreliable_car.drive(80)} km")

    # test_car should only drive sometimes when drive method is executed multiple times for random distances.
    test_car = UnreliableCar("Test car", 150, 45)
    for i in range(1, 10):
        print(f"{test_car} drove {test_car.drive(i)} km")


main()
