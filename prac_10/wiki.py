"""
CP1404/ CP5632 - Practical 10
Extract data from wikipedia using API
"""
import wikipedia

MENU = "(P)age title / Search phrase: "


def main():
    """Display the details on wikipedia for user input search text/ title."""
    page_title = input("Page title / Search phrase: ")
    while page_title != '':
        page = wikipedia.page(page_title)
        print(f"Summary of {page} is : {page.summary}")
        page_title = input("Page title / Search phrase: ")
    print("Have a good day!")


main()
