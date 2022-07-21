# SEQUENCES

# sequences are things that you can iterate over

# create a tuple to hold male friends
# tuple cannot be changed
male_friends = ("Joey", "Ross", "Chandler")
print(male_friends)
print(type(male_friends))

# create a list to hold the female friends
# List can be changed
female_friends = ["Monica", "Phoebe", "Rachel"]
print(female_friends)
print(type(female_friends))

# replace Ross with Kena
new_male_friends = list(male_friends)
new_male_friends[1] = "Kena"
print(new_male_friends)
