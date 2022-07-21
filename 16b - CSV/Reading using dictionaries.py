
import csv

with open("/Users/ikenna/Documents/GitHub/Python/16b - CSV/cats.txt") as cat_file:

    # create a CSV reader
    reader = csv.reader(cat_file)

    # discard the header
    _ = next(reader)

    # create a dictionary to hold the cats
    cats = {} # {} denotes dictionary or set and python determines which from context

    # loop over the rows
    for row in reader:

        # unpack this row
        cat_name,colour,dob = row

        # add this to the dictionary
        cats[cat_name] = (colour,dob)

# print out the dictionary
for key,value in cats.items():

    print(key, value)

# specific cat
print(cats["Neo"])
