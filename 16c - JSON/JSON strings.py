
import json

potter_list = (
    ("Hermoine", "Granger", "Gryffindor", 4),
    ("Draco", "Malfo", "Slytherin", 7),
    ("Harry", "Potter","Gryffindor", 6),
)  

# write to a string variable
characters = json.dumps(potter_list)

# read back in
potter_characters = json.loads(characters)

print(type(potter_characters), potter_characters)

# load and dump writes information and reads it back from a file

# loads and dumps writes and reads it back from a string variable




