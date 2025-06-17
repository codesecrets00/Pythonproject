import numpy as np
x=  [1,2,3]
y = [4,5,6]

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
# arr = np.concatenate(x, y)
arr = np.concatenate((arr1,arr2))
print(arr)