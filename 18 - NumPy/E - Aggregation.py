# similar to row and column totals but more powerful. Allows you to not only sum information but also takes the avg and min. Can be combined with slicing

import numpy as np

# premier league array
prem_table = np.array([ # A two dimensional array
    [2,27,5,6,83,32,86], # a list of list array
    [3,21,11,6,73,44,74],
    [1,20,9,9,68,42,69],
    [0,19,10,9,58,36,67],
    [4,20,6,12,68,50,66]
])

# sum, mean, max, min
print(prem_table[:,-3:-1])

# sum down the first axis
goals = prem_table[:,-3:-1].sum(0) # putting 0 as the sum argurment sum down each column while putting 1 sums across each row

# repeat this
print(goals.sum())