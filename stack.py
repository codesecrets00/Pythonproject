import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# Stack function to put an array over an array
# arr= np.stack((arr1, arr2), axis=1)
# print(arr)

# Stacking along rows use hstack method
# arr = np.hstack((arr1, arr2))
# print(arr)

# Using vstack to stack along columns
# arr = np.vstack((arr1, arr2))
# print(arr)

arr = np.dstack((arr1, arr2))
print(arr)