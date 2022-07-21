
import csv
from datetime import datetime


from pyparsing import col

# opem the text file for reading
with open("/Users/ikenna/Documents/GitHub/Python/16b - CSV/cats.txt") as cat_file:

    # create a CSV reader based on this
    reader = csv.reader(cat_file)

    # read in the header
    header = next(reader)

    # print(header)

    for row in reader:

        cat_name, colour, dob = row
        
        # extract the date as a date
        date_of_birth = datetime.fromisoformat(dob)
        print("{0} is {1} was born in {2}".format(cat_name,colour,datetime.strftime(date_of_birth, "%B %Y")))
