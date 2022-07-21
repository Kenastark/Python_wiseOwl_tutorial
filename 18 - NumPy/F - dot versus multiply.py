
import numpy as np

# the first matrix
matrix_a = np.array([
    [2,3],
    [1,5]
])

# the second matrix
matrix_b = np.array([
    [4,7],
    [6,0]
])

print("\nMatrix A")
print(matrix_a)

print("\nMatrix B")
print(matrix_b)

# cell-by-cell multiplication
answer_1 = np.multiply(matrix_a,matrix_b)
print("\nMultiply function")
print(answer_1)

# matrix multiplication
answer_2 = matrix_a.dot(matrix_b)
print("\nDot function")
print(answer_2)