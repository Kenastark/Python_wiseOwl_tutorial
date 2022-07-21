print("STARTED......")
# create empty list
items = []

# read in the file
with open(r"/Users/ikenna/Desktop/Shopping list.rtf") as shop_file:

    # read in the lines
    for line in shop_file:

        # add to my list
        items.append(line.strip().replace("\\", '').replace("\t", ''))


# print out the initital list
# print("Initial list".ljust(20) + repr(items))

# remove duplicate
items_set = set(items)
print("Revised list".ljust(20) + repr(items_set))

# sprt this as a list
item2 = list(items_set)
item2.sort()

print("Final list".ljust(20) + repr(item2))


print("ENDED....")