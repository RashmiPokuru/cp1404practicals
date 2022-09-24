"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_LOW = 0.1
BONUS_HIGH = 0.15
SALES_THRESHOLD = 1000
sales = float(input("Sales : $"))
while sales >= 0:
    if sales < SALES_THRESHOLD:
        bonus = sales * BONUS_LOW
    else:
        bonus = sales * BONUS_HIGH
    print(f"Bonus : ${bonus:.2f}")
    sales = float(input("Sales : $"))
