"""CP1404/CP5632 Practical - Guitar class.
Estimate = 2 hours
Current_time = 4:46 PM
Actual duration =
"""


class Guitar:
    """Represent a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """
        Construct a Guitar from the given values
        name: string, name of guitar
        year: integer, year of guitar
        cost: float, cost of guitar
        """
        self.name = name
        self.year = year
        self.cost = cost
