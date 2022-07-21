
with open(r"/Users/ikenna/Desktop/Best films ever.rtf", "r") as movie_file:

    # loop over each line
    for line in movie_file:

        bits = line.split(" - ")

        # unpack this
        film_number, film_name = bits

        # print this out
        print(film_number, film_name.strip())
movie_file.close()