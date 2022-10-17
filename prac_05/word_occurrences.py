"""
CP1404/CP5632 Prac 05
count the occurrences of words in an input string
Estimate : 30 minutes
Actual :
"""
text = input("Text: ")
word_to_count = {}
words = text.split()
print(words)
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
print(word_to_count)
