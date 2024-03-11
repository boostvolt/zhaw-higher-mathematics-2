import numpy as np

def lagrange_int(x,y,x_int):
    p = 0
    i = 0
    for i in range(np.size(x)):
        j = 0
        l = 1
        for j in range(np.size(x)):
            if(i != j):
                l *= (x_int - x[j] )/ (x[i] - x[j])
        p += l * y[i]

    return p

x = np.array([0,2500,5000,10000])
y = np.array([1013,747,540,226])
x_int = 3750
y_int = lagrange_int(x,y,x_int)

print(y_int)



""" import numpy as np
from scipy.interpolate import lagrange
x = np.array([0,2500,5000,10000])
y = np.array([1013,747,540,226])
poly = lagrange(x, y)
print(poly(3750)) """