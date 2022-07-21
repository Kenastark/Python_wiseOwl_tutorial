# emumerate is used to number each item in the sequence


# Wise owl cats
cats = "Annie,Neo,Salem,Sabrina,Mary,Agatha"

# split cat
cat_list = cats.split(",")
# print(cat_list)
 
# which cat in Neo?
# print(cat_list.index("Neo"))

# list cats with numbers
for cat_number, cat_name in enumerate(cat_list):
    print("cat number {0} is {1}".format(cat_number+1,cat_name))

