
# a quotation from "Animal farm" by george orwell
from urllib.parse import quote_plus


quote = "Who controls the past controls the future. Who controls the present controls the past."

# # split it into different words
# words = quote.split()

# # reverse the quote
# words.reverse()

# # join words together
# back_quote = " ".join(words)

# print(back_quote)

# partition like split allows you to split something into 3 parts based on the first occurence of the character you set.
# One part before the character you set
# secong part is the character you set
# the third part is the part after the charater you set

# r partition splits by the last occurance of the character you set
sentences = quote.rpartition(".")
for sentence in sentences:
    print(sentence)


