
# assigning strings
author_name = "George Orwell"

# report strings
chant_part_1 = "Oggy! " * 3
chant_part_2 = "O1! " * 3

# concatenating strings
chant = chant_part_1 + chant_part_2
print(chant)

# get lenght of it
lenght_chant = len(chant)
print(lenght_chant)

# strings are case sensitive
number_g = author_name.lower().count("g")
print(number_g)