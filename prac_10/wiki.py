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
        try:
            page = wikipedia.page(page_title, auto_suggest=False)
            print(f"Summary of {page} is : {page.summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        page_title = input("Page title / Search phrase: ")
    print("Have a good day!")


main()
