
import datetime
from time import strftime

actors = {
    "Meryl streep": datetime.datetime(1949,6,22),
    "Tom Cruise": datetime.datetime(1962,7,3),
    "Ana de Armas": datetime.datetime(1988,4,30),
    "Bruce Willis": datetime.datetime(1955,3,20)

}

# Emma Stone
actors["Emma Stone"] = datetime.datetime(1988,11,6)

# change Bruce dob
actors["Bruce Willis"] = datetime.datetime(1955,3,19)

# remove item from the list
del actors["Tom Cruise"]

# add kena
actors["Ikenna Udeani"] = datetime.datetime(1998,9,2)

# listing out the items
for actor_name,dob in actors.items():
    # print(type(actor_name), type(dob))

    print(actor_name,dob,strftime("%b %d %Y"))












