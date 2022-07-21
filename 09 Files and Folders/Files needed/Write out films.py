
worst_films = ["Titanic","Twilight"]

with open(r"c:\__work\python\tutorial\bad_films\bad films.txt","a") as bad_file:

    # title
    bad_file.write("WORST FILMS EVER?\n")

    # write out my worst film
    bad_file.write("Home Alone\n")

    # write out Andrew's
    bad_file.writelines("\n".join(worst_films))

print("Done!")
