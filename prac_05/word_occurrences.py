"""
CP1404/CP5632 Prac 05
count the occurrences of words in an input string
Estimate : 30 minutes
Actual : 28 minutes
"""
word_to_count = {}
text = input("Text: ")
words = sorted(text.split())
# print(words)


for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
# print(word_to_count)


try:   # handle empty string input
    maximum_word = max([len(word) for word in word_to_count.keys()])
    for word, count in word_to_count.items():
        print(f"{word:{maximum_word}} : {count}")
except ValueError:
    print("Empty invalid string")


