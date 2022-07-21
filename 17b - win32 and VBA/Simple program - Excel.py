
import win32com.client

# launch Excel
xl = win32com.client.Dispatch("Excel.Application")

# make it visible
xl.visible = True

# create a new workbook
new_book = xl.Workbooks.Add()

# type name into A1
xl.Range("A1").value = "Ikenna Udeani"




