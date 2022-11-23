"""
CP1404/CP5632 Practical 09
Band class
"""


class Band:
    """Band class with musicians and instruments."""

    def __init__(self, name=""):
        """Initialize Band with empty collections of musicians and instruments."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of Band."""
        return f"{self.name} ({','.join(str(musician) for musician in self.musicians)})"

