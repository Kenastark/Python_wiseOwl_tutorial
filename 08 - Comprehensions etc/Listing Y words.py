#  a list comprehension is just a loop condensed into a single line of text


# from Mark Zuckerberg
quote = "The biggest risk is not taking any risk...the only strategy that is guaranteed to fail is not taking risks."

# without comprehension
words = quote.split()
# for word in words:
#     if "y" in word.lower():
#         print(word[::-1])

#  with comprehension
back_y_words =[word[::-1]for word in words if "y" in word.lower()]


for w in back_y_words:
    print(w)







