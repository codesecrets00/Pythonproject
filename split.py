import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])


# split array using array_split method
# new_array = np.array_split(arr, 3)
# print(new_array)

# Spliting array using array_split method with axis 1
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
# new_array = np.array_split(arr1, 2, axis=1)
# print(new_array)

# Spliting array using hsplit method
# new_array = np.hsplit(arr1, 1)
# print(new_array)

# spliting array using vsplit method with axis 1
# new_array = np.vsplit(arr1, 3)
# print(new_array)

arr2 = arr.reshape(3,3,1)
# print(arr2)
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr3.base)
print(arr3.shape)

# spliting array using dsplit method 
new_array = np.dstack(arr3)
print(new_array)