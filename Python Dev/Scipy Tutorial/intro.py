from scipy.spatial.distance import pdist, squareform
import numpy as n

x = n.array([1, 2, 3, 4])
y = n.array([2, 4, 5, 6])
z = n.hstack((x, y))
v = n.concatenate((x, y), axis=0)
d = n.array([[1, 2], [3, 4], [2, 4], [6, 8]])
# print(z, v)

a = n.array([1, 2, 3])
b = n.array([4, 5, 6])
c = n.c_[a[None, :], b[None, :]]
# print(c)

dist = pdist(d, 'euclidean')
print dist
print squareform(dist)