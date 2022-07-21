
# Wise owl cats
cats = "Annie,Neo,Salem,Sabrina,Mary,Agatha"

# split cat
cat_list = cats.split(",")
print(cat_list)


# join list back
rejoined_list = " | ".join(cat_list[-1::-1])
print(rejoined_list)

