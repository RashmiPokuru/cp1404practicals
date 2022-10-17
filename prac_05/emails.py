"""
CP1404/CP5632 Prac 05
extract name from input
get name if user does not press y or enter
print emails and names
Estimate : 30 minutes
Actual : 40 minutes
"""


def main():
    """print emails and names from input"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        name_indicator = input(f"Is your name {name}? (Y/n) ").lower()
        if name_indicator not in "y":
            name = input("Name: ")
        email_to_name[email] = name.title()
        email = input("Email: ")

    print(email_to_name)

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """extract name from email"""
    name = ' '.join(email.split('@')[0].split('.'))
    return name


main()
