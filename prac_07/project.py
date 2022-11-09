"""
CP1404/CP5632 Practical - Project class
Estimate - 2 hours
"""
import datetime


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
        return f"{self.name}, start: {datetime.datetime.strftime(self.start_date, '%d/%m/%Y')}," \
               f" priority {self.priority}, estimate: ${self.cost_estimate:.2f}, " \
               f"completion: {self.completion_percentage}%"

    def __repr__(self):
        """return list objects in string format"""
        return str(self)

    def is_complete(self):
        """Return true or False if completion percentage is 100 or not"""
        return self.completion_percentage == 100

    def __lt__(self, other):
        return self.priority < other.priority


def run_tests():
    p1 = Project(name="Build Car Park", start_date=datetime.datetime.strptime("9/1/2021", '%d/%m/%Y'), priority=2,
                 cost_estimate=600000.0,
                 completion_percentage=95)
    p2 = Project(name="Test", start_date=datetime.datetime.strptime("9/2/2021", '%d/%m/%Y'), priority=3,
                 cost_estimate=700.0,
                 completion_percentage=100)
    print(p1)
    print(p1.is_complete())
    print(p2)
    print(p1.is_complete())
    print(p1 < p2)


if __name__ == '__main__':
    run_tests()
