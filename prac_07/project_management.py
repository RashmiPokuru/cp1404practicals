"""
CP1404/CP5632 Practical - Program to load and save a data file and use a list of Project objects.
Estimate - 2 hours
"""
from prac_07.project import Project
import datetime
import operator

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate " \
       "project\n(Q)uit"
FILE_NAME = "projects.txt"
HEADER = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"


def main():
    projects = load(FILE_NAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            file_name = input("Enter the file name to load from: ")
            projects = load(file_name)
            print(f"{len(projects)} from {file_name} are loaded")
        elif choice == "S":
            file_name = input("Enter the file name to save to: ")
            save(projects, file_name)
            pass
        elif choice == "D":
            display(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add(projects)
        elif choice == "U":
            update(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
        save(projects, FILE_NAME)
    print("Thank you for using custom-built project management software.")


def load(file_name):
    projects = []
    with open(file_name, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            # print(parts)
            # parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], datetime.datetime.strptime(parts[1], "%d/%m/%Y").date(),
                              int(parts[2]), float(parts[3]), float(parts[4]))
            # print(project)
            projects.append(project)
        # print(projects)
    return projects


def display(projects):
    print("Incomplete projects: ")
    incomplete_projects = [project for project in projects if not project.is_complete()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(project)
    print("Completed projects:")
    completed_projects = [project for project in projects if project.is_complete()]
    completed_projects.sort()
    # print(completed_projects)
    for project in completed_projects:
        print(project)
    # print(projects)


def update(projects):
    for i, project in enumerate(projects):
        print(i, project)
    update_choice = int(input("Project choice: "))
    print(projects[update_choice])
    try:
        new_percentage = float(input("New Percentage: "))
        projects[update_choice].completion_percentage = new_percentage
    except ValueError:
        pass
    try:
        new_priority = int(input("New Priority: "))
        projects[update_choice].priority = new_priority
    except ValueError:
        pass
    # print(projects)


def add(projects):
    print("Let's add a new project")
    project_name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(project_name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def filter_projects(projects):
    minimum_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yy): "),
                                              "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > minimum_date]
    filtered_projects.sort(key=operator.attrgetter("start_date"))
    for project in filtered_projects:
        print(project)


def save(projects, file_name):
    with open(file_name, "w") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(project.name, project.start_date, project.priority, project.cost_estimate,
                  project.completion_percentage, sep=',', file=out_file)


# load(FILE_NAME)

main()
