
integers = range(1,21)


#  list of Kena's dozen favorite films
films = (

    "Cabaret", "The Matrix", "The Parent Trap", "The Sound of Music",
    "Laa Laa land", "The Prestige", "Love Actually", "Raiders of the Lost Ark",
    "12 Angry Men", "Die Hard", "A Few Good Men", "Casablanca"
)

quote = "First they come for the socialists, and I did not speak out - because I was not a socialist. Then they came for the trade unionist, and I did not speak out - because I was not a trade unionist. Then they came for the Jews, and I did not speak out - because i was not a Jew. Then they came for me - and there was no one left to speak for me"


# # even numbers
# for num in integers[1::2]:
#     print(num)


#  print every fifth film
# print(films[::5])


# # quote backwards
# start = quote[:10]
# print(start[-1::-1])

# blowing your mind
print(quote.split()[5][-2::-1])

