
quotation = "And we danced, on the brink of an unknown future, to an echo from a vanished past."

# remove punctutation
import string
ttable = str.maketrans('','',string.punctuation)

clean_quote = quotation.translate(ttable)

print(clean_quote)

print("Number of letters = " + str(len(clean_quote)))

letter_set = set(clean_quote) 
print(letter_set)
# python always considers a string of text to be
# a list of the individual characters. So python converts 
# the string clean_quote into a set of individual characters

print("The Number of unique letters = " + str(len(letter_set)))

words = clean_quote.split(" ")
print(words)
print("The number of words are = " + str(len(words)))

# how many of them are unique
words_set = set(words)
print("The Number of unique words = " + str(len(words_set)))

