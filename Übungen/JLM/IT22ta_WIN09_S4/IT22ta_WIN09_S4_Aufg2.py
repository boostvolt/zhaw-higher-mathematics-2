import numpy as np


# Lagrange-Interpolation
def lagrange_int(x, y, x_int):
    p = 0
    n = len(x)

    for i in range(0, n):
        l_n = 1
        for j in range(0, n):
            if j != i:
                l_n *= (x_int - x[j]) / (x[i] - x[j])
        p += y[i] * l_n
    return p


# Gegebene Werte
x = np.array([0, 2500, 5000, 10000])
y = np.array([1013, 747, 540, 226])
x_int = 3750
y_int = lagrange_int(x, y, x_int)

# Ergebnis
print(y_int)

"""
from scipy.interpolate import lagrange
x = np.array([0,2500,5000,10000])
y = np.array([1013,747,540,226])
poly = lagrange(x, y)
print(poly(3750)) 
"""
