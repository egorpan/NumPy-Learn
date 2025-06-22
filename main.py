import numpy as np
a = np.random.randint(0,101,size=15)
print(a[(a>30) & (a<70)])