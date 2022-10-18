"""
CP1404/CP5632 Prac 05
Game, Set, Match
Process wimbledon.csv and display information
estimate = 45 min
Actual = 55 min
"""
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2
FILE_NAME = "wimbledon.csv"


def main():
    """Process csv file and display information of champions and countries"""
    matches = get_matches()
    # print(matches)
    champion_to_count, countries = process_matches(matches)
    display_information(champion_to_count, countries)


def display_information(champion_to_count, countries):
    """Display champions and countries information"""
    print("Wimbledon champions")
    for champion, count in champion_to_count.items():
        print(champion, count)
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


def process_matches(matches):
    """Process matches and return countries, champions to their number of wins"""
    countries = set()
    champion_to_count = {}
    for match in matches:
        champion = match[CHAMPION_INDEX]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
        countries.add(match[COUNTRY_INDEX])
    return champion_to_count, countries


def get_matches():
    """Get matches from the CSV file"""
    matches = []
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            matches.append(line.strip().split(','))
    return matches


main()
