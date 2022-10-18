"""
CP1404/CP5632 Prac 05
get code from input colour name
"""

COLOUR_TO_CODE = {"BlueViolet": "#8a2be2", "Burlywood1": "#ffd39b", "Burlywood": "#deb887",
                  "Carmine Pink": "#eb4c42", "Pink1": "#ffb5c5", "Ruby": "#e0115f", "Silver Pink": "#c4aead",
                  "Snow4": "#8b8989", "SteelBlue": "#4682b4", "Zomp": "#39a78e"}
# print(COLOUR_TO_CODE)

# COLOUR_UPPER_TO_CODE = {colour.upper():code for (colour, code) in COLOUR_TO_CODE.items()}
# print(COLOUR_UPPER_TO_CODE)

colour = input("Enter colour name: ")
while colour != "":
    code = {colour.upper(): code for colour, code in COLOUR_TO_CODE.items()}.get(colour.upper())
    print(f"The code for '{colour}' is {code}")
    colour = input("Enter colour name: ")
