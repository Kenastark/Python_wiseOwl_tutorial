
import openpyxl

# open up the films workbook
films_book  = openpyxl.load_workbook("/Users/ikenna/Documents/GitHub/Python/17a - openpyxl/List of films.xlsx")

# films sheet
film_sheet = films_book["Films"]

# loop over all of the cells in the first column of ids
for cell in film_sheet["A2:A11"]:

    # get the title and the duration in minutes
    title = cell[0].offset(0,1).value
    minutes = cell[0].offset(0,5).value

    # print this out
    print("{0} lasted {1} minutes".format(title,minutes))





