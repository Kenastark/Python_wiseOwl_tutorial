
# 3 random addresses
addresses = "10 Downing Street, London SW1A 2AA\nTHe Shard, London SE1 2NY \nBBC HQ, London W1A 1AA"

import re

postcode_mask = r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}'

postcodes = re.findall(postcode_mask,addresses)
for postcode in postcodes:
    print(postcode)