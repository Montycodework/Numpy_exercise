import numpy as np

#1d array
# a =  np.array([4,7,9])
# print(a[0])

#2d array
# b = np.array([[1,2],[3,4],[5,6]])
# print(b.ndim) # 2d
# print(a.ndim) # 1d
#
#
# print((a.itemsize)) # 4 bytes per item
# print((b.itemsize)) # 4 bytes per item
#
# print(a.dtype) # int32

# b = np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
# print(b)
# print(b.itemsize)


# print(b.size)
#
# print(b.shape)

# -------------------------------------------


# c = np.zeros((3,4))
# print(c)

# c = np.ones((3,4))
# print(c)


# e = np.arange(1,10,2)
# print(e)


# f = np.linspace(1,5, 10)
# print(f)
'''[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
 3.66666667 4.11111111 4.55555556 5.        ]'''


# b.reshape(2,3)
# print(b)

# print(b.ravel()) # To flatten the array in one dimension (do not print it in next line until u capture it another variable )
# print(b) # it will give same old 2d array


# print(b.min())
# print(b.max())
# print(b.sum())

# axis -> 0 horizontal (rows)
# print(b.sum(axis=0))
# output: [ 9. 12.]

# axis -> 1 verticle (columns)
# print(b.sum(axis=1))
# output: [ 3.  7. 11.]


# if you wanted to get square root you can't apply it on an array
# youhave to apply using np

# b.sqrt() - wrong

# print(np.sqrt(b))
'''[[1.         1.41421356]
 [1.73205081 2.        ]
 [2.23606798 2.44948974]]'''


# for matrix
# c = np.array([[1,2],[3,4]])
# d = np.array([[5,6],[7,8]])
# print(c.dot(d))
'''[[19 22]
 [43 50]]'''

