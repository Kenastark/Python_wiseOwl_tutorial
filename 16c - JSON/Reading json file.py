
import json

# read in the file
with open("/Users/ikenna/Documents/GitHub/Python/16c - JSON/sorting hat.json", "r") as json_file:

    # load JSON data into variable
    potter_people = json.load(json_file)

print(type(potter_people))
# test this
for character in potter_people:

    # print first and last name
    print( " ".join((character[0:2])))
