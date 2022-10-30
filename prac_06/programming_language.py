"""CP1404/CP5632 Practical - ProgrammingLanguage class.
Estimate = 30 minutes
Current_time = 3:41 PM
Actual duration = 1 hour
"""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.
        name : string, name of programming language
        typing: string, type of typing of programming language
        reflection: boolean, reflection of programming language
        year: integer, year of programming language
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string format of programming language details"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Returns True/False if the programming language is dynamically typed or not."""
        return self.typing == "Dynamic"


def run_tests():
    """Run tests for the ProgrammingLanguage class"""
    test = ProgrammingLanguage("test", "Static", True, 2022)
    print(test)


if __name__ == '__main__':
    run_tests()
