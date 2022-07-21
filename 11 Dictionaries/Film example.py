
# Title,Certificate,Director,Oscars,Minutes,Released
# Evan Almighty,PG,Tom Shadyac,0,95,2007
# Transformers,12A,Michael Bay,0,144,2007
print("STARTED.............")
films = {}

with open("/Users/ikenna/Documents/GitHub/Python/11 Dictionaries/Movies.csv") as movie_file:

    # read in the lines
    lines = movie_file.read().splitlines()[1:]
    # print(lines)


    for line in lines:
        bits = line.split(',')
        # print(bits)

        # add this film to dictionaries
        films[bits[0]] =  bits[1:]

# print out what you've done
sorted_films = sorted(films)
# print(sorted_films)

# loop over title
for title in sorted_films:

    # get the dictionary value
    value = films.get(title)

    # unpack the list to get default
    cert, dir, oscars, mins, released = value

    # print
    print(title,cert,dir,mins)











