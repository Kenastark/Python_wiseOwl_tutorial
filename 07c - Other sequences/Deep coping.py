
cats = [
    ["Annie","Andy/Jenny"],
    ["Neo", "Andy/Jenny"],
    ["Salem","Sam"],
    ["Sabrina","Sam"],
    ["Marv","Shaun"],
    ["Agatha","Shaun"]

]

# copy the list
import copy
copy_cats = copy.deepcopy(cats)

# change Neo's name
cats[1][0] = "Sprout"

print(id(cats))
print(id(copy_cats))

print(cats)
print(copy_cats)

# when you have a list which contains other list and you do a copy
# instead of copying absolutely everything, it copies things at the highest level
# of the hierarchy

# a deep copying copies everything at the top and also things in the sublists and copy them too




