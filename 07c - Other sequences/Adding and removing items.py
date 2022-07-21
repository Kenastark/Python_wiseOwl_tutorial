
# create a list
wizards = []

# add a couple of wizards
wizards.insert(0,"Harry")
wizards.insert(0,"Hermoine")


# append an item adds an item to the end of the list
wizards.append("Ron")

# death eaters
death_eaters = ["Lucius", "Barty", "Bellatrix"]

# extend my list
# extend adds all the items in the second list into the first one
wizards.extend(death_eaters)

# remove an item
wizards.remove("Barty")

# pop an item removes an item
# you specify the position of the item you want to remove
# you get a reference to the item at the end of it

# popping removes an item from the list but also gets access to the item

bella = wizards.pop(-1)

# clear a list
wizards.clear()

print(bella)
print(wizards)


