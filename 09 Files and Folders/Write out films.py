
worst_films = ["Titanic", "Twilight"]

with open(r"/Users/ikenna/Desktop/bad films.rtf", "w") as bad_file:
    
    # title
    bad_file.write("WORST FILM EVER?\n")

    # write out my worst film
    bad_file.write("Home Alone\n")

    # wite out Andrew's
    bad_file.writelines("\n".join (worst_films))# loops over all the items in the list, writing out one line for each

print("Done!")
bad_file.close()


