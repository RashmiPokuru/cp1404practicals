"""
CP1404/CP5632 - Prac_02
determine score status with function
"""
from random import randint


def main():
    """get score and display its status"""
    user_score = float(input("Enter score: "))
    print(f"status of score {user_score} : {determine_status(user_score)}")
    random_score = randint(0, 100)
    print(f"status of random score {random_score} : {determine_status(random_score)}")


def determine_status(score):
    """determine status based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
