import numpy as np

# iterating element in on dimensional array 
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x = arr.reshape(2, 3, 2)

for a in arr:
    print(a)

# iterating element in 2 dimensional array 
y = arr.reshape(2,6)
for b  in y :
    print(b)

# itereating element in 3 dimensional array
for c in x :
    print(c)