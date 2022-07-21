
file_path = "/Users/ikenna/Documents/GitHub/Python/12b Advanced functions/Files/"

# empty list
lines = []

def read_file(*genres:str) -> None: # the * means is that the argument has an infinite possible lenght

    # looping over all the genres
    for genre in genres:

        # read the file
        with open(file_path + genre + ".csv") as genre_file:

            genre_lines = genre_file.read().splitlines()[1:]

            # add these lines
            lines.extend(genre_lines)

# read in lines from one file
read_file("animation","comedy","musical")

# print the line
for line in lines:
    print(line)











