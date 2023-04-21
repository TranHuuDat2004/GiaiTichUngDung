import numpy as np
array1 = np.array([0, 10, 20, 30, 60])
print("Array1: ",array1)
array2 = [10, 30, 40]
print("Array2: ",array2)
print("Giá trị chung giữa hai phần tử là:")
print(np.intersect1d(array1, array2))
