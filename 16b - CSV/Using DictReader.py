
import csv

with open("/Users/ikenna/Documents/GitHub/Python/16b - CSV/cats.txt") as cat_file:

    # create a dcitionary reader
    cats = csv.DictReader(cat_file) # what this does is read through the lines in the csv file and read each of them into the dictionary

    # print these lines
    for cat in cats:

        print(type(cat), cat) # It does not include it headers bc it automatically detects that it should be used to create the names for the dictionary keys








