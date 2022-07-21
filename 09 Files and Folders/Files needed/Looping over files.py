
import glob

# create a variable to hold the list of files
files = glob.glob(r"C:\__work\Python\tutorial\09 - Files and folders\\**\*.py",recursive=True)

# loop over these files
for file in files:
    print(file)