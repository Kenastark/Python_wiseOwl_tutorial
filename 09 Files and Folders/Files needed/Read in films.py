
with open(r"c:\__work\python\tutorial\Best films ever.txt","r") as movies_file:

    # loop over each line
    for line in movies_file:
        
        bits = line.split(" - ")

        # unpack this
        film_number, film_name = bits

        # print this out
        print(film_number,film_name.strip())


