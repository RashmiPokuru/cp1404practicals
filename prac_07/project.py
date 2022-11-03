"""
CP1404/CP5632 Practical - Project class
Estimate - 2 hours
"""


class Project:
    """Represent a project"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a project"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return formatted project as string"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"


def run_tests():
    p = Project(name="Build Car Park", start_date="12/09/2021", priority=2, cost_estimate=600000.0,
                completion_percentage=95)
    print(p)


run_tests()
