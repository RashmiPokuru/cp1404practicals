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
