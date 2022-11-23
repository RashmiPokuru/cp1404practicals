"""
CP1404/CP5632 Practical 09
SilverServiceTaxi class - class extends Taxi class.
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi is Taxi with new fanciness attribute."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize SilverServiceTaxi class with."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness


