
# the first 20 numbers
integers = range(1,21)

# Python numbers them as
# 0 1 2 3 4 5 6 7 8 9 10 11 12...

#  list of Kena's dozen favorite films
films = (

    "Cabaret", "The Matrix", "The Parent Trap", "The Sound of Music",
    "Laa Laa land", "The Prestige", "Love Actually", "Raiders of the Lost Ark",
    "12 Angry Men", "Die Hard", "A Few Good Men", "Casablanca"
)

# strong containing quotation from Martin Niemoller
quote = "First they come for socialist, and I did not speak out - because I was not a socialist. Then they came for the trade unionist, and I did not speak out - because I was not a trade unionist. Then they came for the Jews, and I did not speak out - because i was not a Jew. Then they came for me - and there was no one left to speak for me"

# first five numbers
# for num in integers[0:5]:
#     print(num)

# # print out first 3 fils
# for film in films[1:4]:
#     print(film)

# last 7 words
words = quote.split()
number_words = len(words)

# for word in words[number_words-7:number_words]:
#     print(word)

# for word in words[-7:]:
#     print(word)

# # first 5 numbers
# for num in integers[:5]:
#     print(num)


# list all films
for film in films[:]:
    print(film)

# word = "wise owl" [1:8:2]
# print(word)