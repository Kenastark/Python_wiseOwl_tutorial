
# partition splits any string of texts into three parts
import sys
paths = sys.path

# loop over paths
for p in paths:
    

    last_bit = p.rpartition("/")
    print(last_bit[-1])