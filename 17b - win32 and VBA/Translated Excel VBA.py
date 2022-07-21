
import win32com.client

# launch excel
xl = win32com.client.Dispatch("Excel.Application")

xl.visible = True

# open the correct workbook
book = xl.workbooks.Open("/Users/ikenna/Documents/GitHub/Python/17b - win32 and VBA/List of films.xlsx")


# get number of Oscars
number_oscars = 42 # input("Enter number of Oscars")

# get name of film
film_name = "Beowulf" # input("Enter the name of film")

# go to the films sheet
book.worksheets("Films").Select

# get where the film is
film_cell = xl.Cells.Find(film_name)

# go to the right-most cell
film_cell = film_cell.End(-4161)

# change number of oscars
film_cell.Getoffset(0, -2).Value = number_oscars
