"""
CP1404/CP5632 Practical - Program to load and save a data file and use a list of Project objects.
Estimate - 2 hours
"""
from prac_07.project import Project

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate " \
       "project\n(Q)uit"
FILE_NAME = "projects.txt"


def main():
    projects = load(FILE_NAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            file_name = input("Enter the file name to load from: ")
            projects = load(file_name)
            # print(projects)
        elif choice == "S":
            file_name = input("Enter the file name to save to: ")
            # save_projects(file_name)
            pass
        elif choice == "D":
            # display_projects()
            pass
        elif choice == "F":
            # filter_projects()
            pass
        elif choice == "A":
            # add_project()
            pass
        elif choice == "U":
            # update_project()
            pass
        else:
            print("Invalid choice")
        # save_projects(projects, FILE_NAME)
    print("Thank you for using custom-built project management software.")


def load(file_name):
    projects = []
    with open(file_name, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            # print(parts)
            projects.append(parts)
    return projects


# load_projects(FILE_NAME)

main()
