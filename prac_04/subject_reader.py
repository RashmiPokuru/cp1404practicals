"""
CP1404/CP5632 Prac_04 - Lists
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        data.append(parts)
    input_file.close()
    # print(data)
    return data


def print_details(data):
    """Prints details of all subjects in readable format"""
    for subject_data in data:
        print(f"{subject_data[0]} is taught by {subject_data[1]:12} and has {subject_data[2]:3} students")


main()
