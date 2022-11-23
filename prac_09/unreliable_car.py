"""
CP1404/CP5632 Practical 09
UnreliableCar class - class extends Car class.
"""
from prac_09.car import Car
from random import randint

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 100


class UnreliableCar(Car):
    """UnreliableCar class extends Car class and has additional reliability attribute."""

    def __init__(self, name, fuel, reliability):
        """Initialise UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability."""
        random_number = randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0  # Return 0 when the car is not driven
        return distance_driven
