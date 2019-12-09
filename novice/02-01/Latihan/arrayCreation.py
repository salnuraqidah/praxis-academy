import numpy as np
from numpy import pi

a = np.array([2,3,4])
print(a)
print(a.dtype)
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)

c = np.array([(15,2,3),(4,5,6)])
print(c)

d = np.array( [ [1,2], [3,4] ], dtype=complex )
print(d)

nol=np.zeros( (3,4) ) #membuat matriks nol
print(nol)

one = np.ones( (2,3,4), dtype=np.int16 ) #membuat matriks satu
print(one)

kosong = np.empty( (2,3) ) #default float64
print(kosong)

mat1 = np.arange( 10, 30, 5 ) #membuat array dari range 10 sampai 30 dengan interval 5
print(mat1)

mat2 = np.arange( 0, 2, 0.3 ) #membuat array dari 0 sampai 2 dengan interval 0.3
print(mat2)

mat3 = np.linspace( 0, 2, 9 ) #2/8=0.25, membuat array dari range 0 - 2 sebanyak 9 number dengan interval 0.25
print(mat3)

x = np.linspace( 0, 2*pi, 100 ) #interval 2*pi/(100-1)
print(x)

f = np.sin(x)
print(f)