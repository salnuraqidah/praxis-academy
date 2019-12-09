import numpy as np

a = np.arange(15).reshape(3, 5) #membuat matriks ukuran 3x5 dengan range 0-14

print(a.shape) #bentuk matriks
print(a.ndim) #dimensi matriks
print(a.dtype.name) #tipe file
print(a.itemsize) #ukuran dalam byte dari setiap elemen array
print(a.size) #jumlah total elemen array
print(type(a))
b = np.array([6, 7, 8])
print(b)
print(type(b))