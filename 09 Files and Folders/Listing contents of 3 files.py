
import glob
print("IT STARTED")
#  create a variable to hold the list of files
files = glob.glob(r"/Users/ikenna/Documents/GitHub/Python/09 Files and Folders/Files needed/**/*.csv",recursive=True )


# sort them into film name order (the hard bit)
files.sort(key = lambda x:x.rpartition("/")[-1:]) #this splits the file path into 1.the part before the final /, 
# 2. the final / and 3. the part after the final forwardslash(/) and split it by the filename using [-1:]

# print a title for the output
print("Number".center(20) + "Country".center(50) + "Area".rjust(20))

# loop over the files
for file in files:
    
    # open each file for reading #looping over a file using glob gives you the full Filepath,f older and the name
    with open(file) as this_file:
        pass
        # get and print the file name for debugging pirposes
        file_path, _, file_name = file.rpartition("/")
        # print(file_path,file_name)

        # get all but the first line
        lines = this_file.read().splitlines()[1:]
        

        # loop over these lines
        for line in lines:

            # split each line into number, country and area, and print out
            number, country, area = line.split(",")

            print(str(number).center(20) + country.center(50) + area.rjust(20))

print("it ENDED")