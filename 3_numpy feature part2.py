import numpy as np

# n = [1,2,3]
# print(n[0:2])


# a = np.array([1,2,3])
# print(a[0:2])
# print(a[-1])

# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b[1,2])

# print(b[0:2,2]) # In the oth row and 1st row we need 2nd element
# [3 6]

# print(b[-1,0:2])
# [7 8]

# print(b[:, 1:3]) # here : means all rows

# for cell in b.flat:
#     print(cell)

# ------------------------------------------
a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)

# print(a)
# print(b)

# print(np.vstack((a,b)))
# print(np.hstack((a,b)))

c = np.arange(30).reshape(2,15)
# print(c)
# print(np.hsplit(c,3))
# print(np.vsplit(c,2))


d = np.arange(12).reshape(3,4)
e = d < 4
print(e)

print(d[e])
d[e] = -1
print(d)


# let's use jupyter notebook now'