"""
CP1404/CP5632 Practical - Test Guitar class
"""
from prac_06.guitar import Guitar


def run_tests():
    """Run tests for Guitar Class"""
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another guitar", 2013, 55555)
    # test __str__(self) method
    print(f"{gibson_guitar} = Gibson L-5 CES (1922) : $16,035.40")
    print(f"{another_guitar} = Another guitar (2013) : $55,555.00")

    # test get_age(self) method
    print(f"Gibson L-5 CES get_age() - Expected 100. Got {gibson_guitar.get_age()}")
    print(f"Another Guitar get_age() - Expected 9. Got {another_guitar.get_age()}")

    # test is_vintage(self) method
    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson_guitar.is_vintage()}")
    print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


run_tests()
