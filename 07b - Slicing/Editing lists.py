
#  list of Kena's dozen favorite films
films = [

    "Cabaret", "The Matrix", "The Parent Trap", "The Sound of Music",
    "Laa Laa land", "The Prestige", "Love Actually", "Raiders of the Lost Ark",
    "12 Angry Men", "Die Hard", "A Few Good Men", "Casablanca"
]

films[4] = "La La Land"

# remove the last two items
films[-2:] = []

#
best_and_worst = films[:2] + films[-2:]

print(best_and_worst)


