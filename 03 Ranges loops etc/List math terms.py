# FORMATTING NUMBERS

# i = 1
# while i <= 10:
#     print("THe cube of {0:2} is {1:4}".format(i, i** 3))
#     i += 1

# print reciprocals
from dis import show_code


i = 1

while i <= 10:
    print("The reciprocal of {0:2} is {1:6.2f}".format(i,1/i))
    i += 1

#         {0:6}
# index number of item : Number of digits to show_code

#             {0:6.2f}
# Index number of item : Number of digits to show . Number of decimal places
# 'f' means it is a floating point number