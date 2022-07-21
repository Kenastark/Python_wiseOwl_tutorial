
def print_info(what:str, **extras) -> None: # The ** specifies a dictionary of extra arguments

    bits = what.split(",")

    link_text = extras["link_text"]
    column_number = extras["column_number"] # "column_number" is a dictionary key

    print(bits[1] + link_text + bits[column_number]) # bits[0] is the first item in the list which is the name of the film

# open csv file
with open("/Users/ikenna/Documents/GitHub/Python/12b Advanced functions/Files/Musical.csv") as csv_file:
    
    
    for line in csv_file.read().splitlines()[1:]:

        # use my function to print this out
        print_info(line,column_number=3,link_text= "lasted for this many minutes: ")





