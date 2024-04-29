import numpy as np

a = 100
b = 0
m = 4

f = lambda v: 97000 / ((-5.0) * (v**2) - 570000.0)


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
        T[k, 0] = sum_trapez(f, a, b, 2**k)

    c = 4
    for k in range(1, m):
        T[0 : m - k, k] = (c * T[1 : m - k + 1, k - 1] - T[: m - k, k - 1]) / (c - 1)
        c *= 4

    print(T)

    return T[0:m]


romberg_extrapolation(f, a, b, m)


a = 100
b = 0
m = 5

f = lambda v: (97000 * v) / ((-5.0) * (v**2) - 570000.0)

romberg_extrapolation(f, a, b, m)
