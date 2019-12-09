import numpy as np

c = np.arange(24).reshape(2,3,4)         # 3d array
print(c.ndim)

print(np.arange(10000))

print(np.arange(10000).reshape(100,100))

np.set_printoptions(threshold=np.nan)