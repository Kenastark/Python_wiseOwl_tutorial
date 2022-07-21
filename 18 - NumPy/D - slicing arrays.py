
import numpy as np

# premier league array
prem_table = np.array([ # A two dimensional array
    [2,27,5,6,83,32,86], # a list of list array
    [3,21,11,6,73,44,74],
    [1,20,9,9,68,42,69],
    [0,19,10,9,58,36,67],
    [4,20,6,12,68,68,66]
])

# # print the first 3 teams
# print("\nFirst 3 teams")
# print(prem_table[0:3:])

# # print out all the key info
# print("\nKey info")
# print(prem_table[:,1:-1]) # the part before the comma is for the row. The part after the comma is the slicing for the column

# # combine this
# print("\nKey info for first three teams")
# print(prem_table[0:3,1:-1])\

# chessboard effect
print("\nAlternate rows and columns")
print(prem_table[0::2,0::2])




