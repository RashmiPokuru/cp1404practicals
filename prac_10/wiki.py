"""
CP1404/ CP5632 - Practical 10
Extract data from wikipedia using API
"""
import wikipedia

MENU = "(P)age title / Search phrase: "


def main():
    """Display the details from wikipedia for user input search text/ title."""
    page_title = input("Page title / Search phrase: ")
    while page_title != '':
        try:
            page = wikipedia.page(page_title, auto_suggest=False)
            print(f"Title: {page.title}\nSummary: {page.summary}\nURL: {page.url}")
        except wikipedia.exceptions.DisambiguationError as e:
            print("Available options:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print("Page doesn't exist. Try another one")
        page_title = input("Page title / Search phrase: ")
    print("Have a good day!")


main()
