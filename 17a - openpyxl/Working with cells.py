
import openpyxl

# create a new workbook
new_book = openpyxl.Workbook()

# get a reference to the active sheet
current_sheet = new_book.active

# write information to the cells
# method 1 - as dictionary

current_sheet["A1"].value = "The meanining of life"

# method 2 - using the cell method
current_sheet.cell(1,2).value = 42

# save this file
new_book.save("/Users/ikenna/Documents/GitHub/Python/17a - openpyxl/Tribute to Douglas Adams.xlsx")

