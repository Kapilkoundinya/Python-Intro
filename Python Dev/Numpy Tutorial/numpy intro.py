import numpy as n

"""
a = n.array([1, 2, 3])
print a[0]
print a.shape
print(a.size)

b = n.array([[1, 2, 3], [3, 4, 5]])
print(b)
print(b.shape)
print(b.size)

c = n.zeros((2, 2))
print c
print(type(c))

d = n.ones((2, 2))
print(d)

e = n.full((2, 2), 1)
print(e)

f = n.random.random((2, 2))
print f



a = n.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print('\n')
b = a[:2, 1:3]
c = a[1:3, :2]
# print c
# print('\n')
# print(a[1, :])
# print(a.shape, a.size)

d = a[:, 2]
print(d, d.shape)
print('\n')
e = a[:, 2:3]
# print(e, e.shape)



a = n.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype='float32')
b = n.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype='float32')
print (a)
# print(b.dtype)
# print(a[a>3])

print (n.add(a, b))
# print(n.divide(a, b))

c = n.array([[1, 2], [3, 4]])
d = n.array([[5, 6], [9,10]])
e = n.array([[2], [4]])
# print(n.dot(c, e))
# print('\n')
# print n.dot(c, d)
# print('\n')
# print n.multiply(c, d)
# print n.sum(c, axis=1)
v = a.T
print (v, v.shape)

"""
# Vector - Matrix addition
b = n.array([[1, 2, 3], [3, 4, 5]])
print(b)
print('\n')
c = n.array([[1, 2, 3]])
print(c)
print('\n')

# Create an empty matrix and add row by row using for loop
x = n.empty_like(b)
for i in range(2):
    x[i, :] = b[i, :] + c
print(x)
print('\n')

# Broadcasting by universal functions(summation is a universal function which supports broadcasting)
d = b + c
print(d)
print('\n')

# Make a new matrix(by stacking the vector) and then add the new matrix to the original matrix
v = n.tile(c, (2, 1))
f = v + b
print f

