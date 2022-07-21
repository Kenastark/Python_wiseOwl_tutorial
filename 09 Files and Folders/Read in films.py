
# open ("filepath name" ,  w or a or r or r+ )
# w means write-only (creates a new file)
# a means Write-only (appends to existing file if one exists, otherwise create a new one)
# r means Read-only. This is the default
# r+ means Read and write

movie_file = open(r"/Users/ikenna/Desktop/Best films ever.rtf", "r")
# lines = movie_file.readline()
# print(lines)

# loop over each line
for line in movie_file:
    # clear_line = line.replace("\n", '').replace(",", '').replace("'", '').replace("\\",'').strip()
    bits = line.split(" - ")
    # print(clear_line)

    # unpack this
    film_number, film_name = bits

    # # print this out
    print(film_number,film_name.strip())

#  close the file
movie_file.close()

