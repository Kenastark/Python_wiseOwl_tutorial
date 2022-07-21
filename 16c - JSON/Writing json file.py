
potter_list = (
    ("Hermoine", "Granger", "Gryffindor", 4),
    ("Draco", "Malfo", "Slytherin", 7),
    ("Harry", "Potter","Gryffindor", 6),
)  

import json

with open("/Users/ikenna/Documents/GitHub/Python/16c - JSON/sorting hat.json", "w") as json_file:

    # dump othe Harry potter info
    json.dump(potter_list,fp=json_file,indent=4) # you can dump list, tuples, dictionaries, dictionaries of lists of tuples provided it is expressible in python


