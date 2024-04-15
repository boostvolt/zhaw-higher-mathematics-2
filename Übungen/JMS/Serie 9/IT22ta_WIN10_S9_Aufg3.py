import numpy as np

f = lambda x: np.cos(x ** 2)
a = 0.0
b = np.pi  
m = 5

def sum_trapez(f, a, b, n):
    h = (b - a) / n
    res = 0
    k = (f(a) + f(b)) / 2
    for i in range(1, n):
        xi = a + i * h
        res = res + f(xi)
    return h * (k + res)

def romberg_extrapolation(f, a, b, m):
    T = np.zeros((m, m))
    
    for k in range(m):
        T[k, 0] = sum_trapez(f, a, b, 2 ** k)

    c = 4
    for k in range(1, m):
        T[0:m - k, k] = (c * T[1:m - k + 1, k -1] - T[:m - k, k -1]) / (c - 1)
        c *= 4

    print(T)

    return T[0:m]

romberg_extrapolation(f, a, b, m)