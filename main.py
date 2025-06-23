import numpy as np

def addition(x,y):
    if x <0:
        return 0
    else:
        return x+y
a = np.array([1,2,3,-1,-20,22,4])
f_vectorization = np.vectorize(addition)
print(f_vectorization(a,5))