
def film_lines(file_path: str, file_name:str) -> list:

    # open the file
    with open(file_path + file_name) as films_file:

        # get all the lines
        lines = films_file.read().splitlines()[1:]
    return lines


# test my function
for line in film_lines("/Users/ikenna/Documents/GitHub/Python/12 Functions/", "musical.csv"):
    print(line)




