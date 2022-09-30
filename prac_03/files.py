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
