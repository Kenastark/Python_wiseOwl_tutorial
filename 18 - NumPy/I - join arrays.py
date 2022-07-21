
import numpy as np

# 2020/21: Man City, Man United, Liverpool, Chelsea, Leicester City
pl_2021 = np.array([ # A two dimensional array
    [2,27,5,6,83,32,86], # a list of list array
    [3,21,11,6,73,44,74],
    [1,20,9,9,68,42,69],
    [0,19,10,9,58,36,67],
    [4,20,6,12,68,50,66]
])

# 2019/20:  Man City, Man United, Liverpool, Chelsea, Leicester City
pl_2020 = np.array([ # A two dimensional array
    [1,32,3,3,85,33,99], # a list of list array
    [2,26,3,9,102,35,81],
    [3,18,12,8,66,36,66],
    [0,20,6,12,69,54,66],
    [4,18,8,12,67,41,62]
])

# # METHOD 1 - Create another dimension
# combined = np.stack([pl_2021,pl_2020],0)
# print(combined)

# METHOD 2 - Glue them together
combined = np.concatenate([pl_2021,pl_2020],0)
print(combined)


