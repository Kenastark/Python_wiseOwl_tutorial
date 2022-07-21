
# wise owl cats
cats = ["Annie","Neo","Salem","Sabrina","Mary","Agatha"]

#  copy list
copy_cats = cats.copy()

# change 2 list
cats.append("Tiddles")
copy_cats.remove("Annie")

# you can use the 'id() function to print out the internal id of where 
# something is stored in memory
# print ids
print(id(cats))
print(id(copy_cats))

# print results
print(cats)
print(copy_cats)



