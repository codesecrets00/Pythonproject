import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
x = arr.view()
x[0]= 100
print(x)
print(arr)
print(x.base)
print(arr.base)