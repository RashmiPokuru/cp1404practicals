"""
CP1404/CP5632 Practical 09
UnreliableCar class - class extends Car class.
"""
from prac_09.car import Car


class UnreliableCar(Car):
    """UnreliableCar class extends Car class and has additional reliability attribute."""

    def __init__(self, name, fuel, reliability):
        """Initialise UnreliableCar"""
        super().__init__(name, fuel)
        self.reliability = reliability
