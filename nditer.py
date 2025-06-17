import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
x = arr.reshape(1,4,2)
print(x)

for a in np.nditer(x):
    print(a) 

# flags buffered is used to add extra spaces

for b in np.nditer(x, flags=['buffered'], op_dtypes='S'):
    print(b)

# Itereating with different step size

y = arr.reshape(2,4)
for d in np.nditer(y[:, ::2]):
    print(d)

# With the help of ndenumerated we iterrate element in the array

for idx, e in np.ndenumerate(x):
    print(idx, e )