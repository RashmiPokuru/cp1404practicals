MENU = """S - Score; R - Print Result; T - Print Stars; Q - Quit"""

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    """get score, print result and stars according to the choice"""
    score = -1
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "S":
            score = get_valid_score("Score : ")
        elif choice == "R":
            print(determine_status(score))
        elif choice == "T":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def print_stars(score):
    """print as many stars as the score"""
    if score == -1:
        print("No score exists")
    else:
        print("*" * score)


def get_valid_score(prompt):
    """get valid score"""
    score = int(input(prompt))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid Score")
        score = float(input(prompt))
    return score


def determine_status(score):
    """determine status based on score"""
    if score == -1:
        return "No score exists"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
