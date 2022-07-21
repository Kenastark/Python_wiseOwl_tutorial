
from re import sub
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
print("\n")
# filter, transpose, flatten, edit, reshape/resize and clip arrays

# filtering: show elements more than 80
# tests = prem_table > 80
# filtered_table = prem_table[tests]
# print(filtered_table)

# transpose method 1: swapping rows and columns
# transposed_table = prem_table.T
# print(transposed_table)

# # transpose method 2:
# transposed_tablle = np.transpose(prem_table)
# print(transposed_tablle)

# flattening: means collapsing an array
# flatten 
# flat_array = prem_table.flatten() #returns a copy of the array
# print(flat_array)

# #ravel
# ravalled_array = np.ravel(prem_table) #returns a contiguous flattened array
# print(ravalled_array)

# # editing
# prem_table[1][2] = 22
# print(prem_table)

# # reshape
# sub_table = prem_table[:,1:]
# # reshaped_table =

# # resizing
# resized_table = np.resize(sub_table,(4,4))
# print(resized_table)


# clip the table
new_table = prem_table.clip(10,50)
print(new_table) 
