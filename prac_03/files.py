"""
CP1404/CP5632 - Prac_03
Files
Writes to the files and then reads them
"""
# 1.

name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()
