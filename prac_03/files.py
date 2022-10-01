"""
CP1404/CP5632 - Prac_03
Files
Writes to the files and then reads them
"""
# 1.
"""Write name to name.txt."""
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
"""Print name in the file"""
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# 3.
"""Read first two numbers from "numbers.txt" file and print total of them"""
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)

# 4.
"""Print total of all lines in file"""
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)



