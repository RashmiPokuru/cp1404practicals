"""CP1404/CP5632 Practical - Guitar class.
Estimate = 2 hours
Current_time = 4:46 PM
Actual duration =
"""
VINTAGE_AGE = 50
CURRENT_YEAR = 2022


class Guitar:
    """Represent a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """
        Initialise a Guitar from the given values
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE
