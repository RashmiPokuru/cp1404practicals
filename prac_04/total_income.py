"""
CP1404/CP5632 Prac 4 - Lists
cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        # income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print list of month's income with cumulative totals"""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print(f"Month {month + 1:2} - Income: ${income:10.2f}         Total: ${total:10.2f}")
        # print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()


