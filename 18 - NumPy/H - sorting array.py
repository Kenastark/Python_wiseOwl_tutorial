
import numpy as np

# premier league array
prem_table = np.array([ # A two dimensional array
    [2,27,5,6,83,32,86], # a list of list array
    [3,21,11,6,73,44,74],
    [1,20,9,9,68,42,69],
    [0,19,10,9,58,36,67],
    [4,20,6,12,68,50,66]
])
print(prem_table)

# sort this array
# new_order = np.sort(prem_table,0)
# print(new_order)

# create a column of sort indices
sort_indices = np.argsort(prem_table[:,2])

print(sort_indices)

final_table = prem_table[sort_indices]
print(final_table)



