import numpy as np
a = np.array([1,22,3,44],dtype="int32")
print(a.dtype)  #print data type

print(a.itemsize)  #

b= np.array([[1,1,1],[1234,1234,1234]])

print(b.size)
print(a.ndim)
print(b.ndim)
