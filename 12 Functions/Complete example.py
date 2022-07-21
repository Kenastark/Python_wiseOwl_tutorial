
from os import nice
import WOL_functions as wol


# test it out
# print(wol.get_age("09/08/2012"))

import glob

for file in glob.glob("/Users/ikenna/Documents/GitHub/Python/12 Functions/*.csv"):
    
    # split file into path and file name
    file_path, _, file_name = file.partition("/")
    print("\n" +file_path,file_name  + "\n")
    print("Title".ljust(30),"Run Time".center(20), "Age".center(6), "Genre".rjust(15))
    # read in that file
    lines = wol.film_lines(file_path + "/" ,file_name)

    # loop over these lines
    for line in lines:

        # ID,Title,Realease Date, Run Time, Genre
        id, title, release_date, run_time, genre = line.split(",")

        # getting a nice run time
        nice_time = wol.get_duration(int(run_time))

        # get the age of the film
        age = wol.get_age(release_date)

        # print it out
        print(title.ljust(30) ,str(nice_time).center(20),str(age).center(6),genre.rjust(15))


