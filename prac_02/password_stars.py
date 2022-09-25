"""
CP1404/CP5632 - Prac_02
Refactor password_stars.py to use functions
"""


MINIMUM_LENGTH = 10


def main():
    """get password and print asterisks"""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """print asterisks as long as the password"""
    print("*" * len(password))


def get_password():
    """Get valid password"""
    password = input(f"Password (minimum length of {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Invalid password. Minimum length of password must be {MINIMUM_LENGTH}")
        password = input(f"Password (minimum length of {MINIMUM_LENGTH} characters): ")
    return password


main()
