import numpy as np

def matrixMultiplication():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 0], [5, 7]])

    if a.shape[1] != b.shape[0]:
        print("Matrix dimensions are incompatible for multiplication.")
        return None

    result = np.dot(a, b)
    return result

c = matrixMultiplication()
print(c)
