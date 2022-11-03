"""
CP1404/CP5632 Practical - Program to load and save a data file and use a list of Project objects.
Estimate - 2 hours
"""
MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n" \
       "(A)dd new project,(U)pdate project"
FILE_NAME = "projects.txt"


def main():
    projects = load_projects(FILE_NAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            file_name = input("Enter the file name to load from: ")
            # load_projects(file_name)
            pass
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


def load_projects(file_name):
    projects = []
    with open(file_name, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.split("\t")
            projects.append(parts)
    print(projects)

    # return load_projects(FILE_NAME)


load_projects(FILE_NAME)

# loading file and menu
