
import glob

# create a variable
files = glob.glob(r"/Users/ikenna/Documents/GitHub/Python/09 Files and Folders/*.py",recursive=True) # add **/ to loop down into the bottom of the tree

#  loop over files
for file in files:
    print(file)

