
import openpyxl

# open up the genre workbook
book = openpyxl.load_workbook("/Users/ikenna/Documents/GitHub/Python/17a - openpyxl/Films by genre.xlsx")

# method 1 - get a list of all the worksheet names
# sheet_names = book.sheetnames

# # loop over all the worksheet names
# for sheet in sheet_names:

#     # get a reference to this worksheet in turn
#     this_sheet = book[sheet]

#     # print out the contents of A1
#     print(this_sheet["A1"].value)

# method 2 -
# bette way to loop over sheets
for s in book: # this will assume that 's' refers to each worksheet at a time
    
    # print out A1 value
    print(s["A1"].value)

# When you refer to a workbook, it assumes its a collection of individual worksheets within it
