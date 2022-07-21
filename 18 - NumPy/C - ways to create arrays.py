
import numpy as np

# arange is the equivalent of the range function
test_array = np.arange(1,11,2)

# linspace which fills range..always generate floating point numbers
test_array = np.linspace(1,10,7)

# empty array
test_array = np.empty((2,3)) # the argument is a shape specified in brackets. The result of this its creates a space in memory but it doesn't initialise any of the values but instead displays whatever was left in memory as if there were numbers

# zaros and ones
test_array = np.zeros((10,))
test_array = np.ones((10,2))

# random numbers
test_array = np.random.rand(2,7) # the numbers return are btw 0 and 1 by default
test_array = np.random.randint(1,11,(3,4,5)) # generates random integers between 1 and 10. The third argument in the shape of the array

# generate an array from a sequence
squares = [n * n for n in range(1,11)]

test_array = np.fromiter(squares,int)


# print out test array
print(test_array)











