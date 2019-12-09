import numpy as np

a = np.array( [20,30,40,59] )
b = np.arange( 4 )

c = a - b
print(c)

d = b**2
print(d)

e = 10*np.sin(a)
print(e)

print(a<35)

A = np.array( [[1,1],
				[0,1]] )
B = np.array( [[2,0],
				[3,4]] )

C = A * B #perkalian antar elemen
D = A @ B #perkalian dot
F = A.dot(B)

a1 = np.ones((2,3), dtype=int)
b1 = np.random.random((2,3))
print(a1+=3)
