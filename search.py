import numpy as np
# Creating an array using numpy array method
arr = np.array([1,2,3,4,5,6,7,8,9])

# Searching an index of arrray using where method
# x = np.where(arr==4)
# print(x)

# x = np.where(arr%2== 0)
# ?print(x)

# Search sorted method to short an array
newarrary = np.array([6,7,8,9])
 x= np.searchsorted(newarrary, [7,9], side='right')
 print(x)