
import glob

# create a variable to hold the list of files
files = glob.glob(r"C:\__work\Python\tutorial\09 - Files and folders\**\*.csv",recursive=True)

# sort them into file name order (the hard bit)
files.sort(key = lambda x:x.rpartition("\\")[-1])

# print a title for the output
print("Number".center(20) + "Country".center(50) + "Area".rjust(20))

# loop over the files
for file in files:

    # open each file for reading
    with open(file) as this_file:

        # get and print the file name for debugging purposes
        file_path, _, file_name = file.rpartition("\\")
        # print(file_path,file_name)

        # get all but the first line
        lines = this_file.read().splitlines()[1:]
       
        # loop over these lines
        for line in lines:

            # split each line into number, country and area, and print out
            number, country, area = line.split(",")

            print(number.center(20) + country.center(50) + area.rjust(20))



            

