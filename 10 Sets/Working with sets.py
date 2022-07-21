
#  friends
friends = {
    
    "Rachael","Phoebe", "Chandler",
    "Joey","Monica","Ross"

}

# shelves
shelves = {"Ronnie-Filchner","Ross","McMurdo"} 

# print(friends)
# print(shelves)

# # prover these are sets
# print(type(friends))
# print(type(shelves))

# union between sets
union = friends | shelves
print(union)

# intersection
intersection = friends & shelves
print(intersection)

# ice shelves which are'nt friends
ice_shelves_not_friends = shelves - friends
print(ice_shelves_not_friends)

# elements in either set, but not both
bob = friends ^ shelves
print(bob)











