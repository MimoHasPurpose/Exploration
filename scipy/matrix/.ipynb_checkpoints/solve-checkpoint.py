import numpy as np 
import scipy
from scipy import linalg
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])
x=linalg.solve(a,b)
print(x)