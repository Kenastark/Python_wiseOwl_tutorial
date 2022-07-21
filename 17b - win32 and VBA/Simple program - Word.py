
import win32com.client

# launch Word
wd = win32com.client.Dispatch("Word.Application")

# make this visible
wd.visible = True

# add a document
wd.Documents.Add()

# type something
wd.Selection.TypeText("Kena")
 



