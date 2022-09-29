"""
CP1404/CP5632 - Prac_03
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# Answers:
# 1. It occurs when either numerator or denominator is not integer (Eg: User enters string)
# 2. It occurs when user enters denominator as zero
# 3. By calculating fraction only when denominator is not zero

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # fraction = numerator / denominator
    # print(fraction)
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")