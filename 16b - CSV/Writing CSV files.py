
import csv

# open up a file for writing
with open("/Users/ikenna/Documents/GitHub/Python/16b - CSV/cats.txt", "w",newline="") as cat_file:

    # create a CSV writer
    writer = csv.writer(cat_file)

    # write out the header
    writer.writerow(["Cat name", "Colour", "Date of birth"])

    # Write out the cats
    writer.writerow(["Annie", "Tortoiseshell", "2019-08-15"])
    writer.writerow(["Neo", "Black and white", "2019-08-15"])

    # finished
    print("That's it!")


