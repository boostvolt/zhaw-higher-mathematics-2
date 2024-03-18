from ctypes.wintypes import HACCEL
import numpy as np

x = np.array([4, 6, 8, 10])
y = np.array([6, 3, 9, 0])
xx = np.array([])

print(y[:-1])

def spline(x, y, xx):
    if (x.size != y.size):
        return "x and y must have the same size"
    a = np.zeros_like(y)
    h = np.zeros_like(len(x) - 1)
    c = np.zeros_like(x)

    for i in range(len(x)):
        a[i] = y[i]
        h[i] = x[i + 1] - x[i]
    
    for i in range(len(c) - 1):
        if (i == 1):
            2 * (h[0] + h[1]) * c[1] + h[1] * c[2] = 


    

    b = ((y[1:] - y[:-1]) / h) - (c[1:] + 2 * c[:-1]) * h/3
    d = (c[1:] - c[:-1]) / (h * 3)


spline(x, y, xx)