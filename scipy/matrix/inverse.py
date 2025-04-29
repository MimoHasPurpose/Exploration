import numpy as np 
import scipy
from scipy import linalg
a=np.array([[1.,2.],[3.,4.]])
b=linalg.inv(a)
axb=np.dot(a,b)
print(np.dot(a,b))
print(b)