
import openpyxl

# open the filns workbook
film_book = openpyxl.load_workbook("/Users/ikenna/Documents/GitHub/Python/17a - openpyxl/List of films.xlsx")

# work with correct worksheet
films_sheet = film_book["Films"] # case sensitive

# changing the oscars
films_sheet["E6"] = 0

# save my changes
film_book.save("/Users/ikenna/Documents/GitHub/Python/17a - openpyxl/List of films.xlsx")

# close this file
film_book.close()