
import numpy as np

# premier league array
prem_table = np.array([ # A two dimensional array
    [2,27,5,6,83,32,86], # a list of list array
    [3,21,11,6,73,44,74],
    [1,20,9,9,68,42,69],
    [0,19,10,9,58,36,67],
    [4,20,6,12,68,50,66]
])

points = np.array([3,1,0])

# subset of the table giving games played
played = prem_table[:,1:4]

# multiply using dot (matrix multiplication)
answer1 = played.dot(points) #this method solves like this [(27*3) + (5*1) + (5*0)] + [(21*3) + (11*1) + (6*0)] + [] + []+ [] + ...
print("MATRIX MULTIPLICATION ANSWER")
print(answer1)
print("\n")


# Games played
print("Games Played","Points for Wins, Draws and Losses".rjust(55))
print(played, str(points).rjust(40))
print("\n")

# cell-by-cell multiplication
answer2 = np.multiply(played, points)# this method solves like 
# [
#   [(27*3) (5*1) (6*0)], 
#   [[21*3) (11*1) (6*0)], etc 
# ]
print("Cell-By-Cell Multiplication of Items".center(20))
print(str(answer2).center(20))
print("\n")

# sum across the row
final_answer = answer2.sum(1)
print("CELL-BY-CELL MULTIPLICATION ANSWER")
print(final_answer)

