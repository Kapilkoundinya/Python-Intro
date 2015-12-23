import numpy as n

a = n.array([[1, 2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 0]])
print(a)
print '\n'

b = n.array([[1], [2], [3]])
print(b.shape)

c = a + b
print(c)
