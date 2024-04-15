import numpy as np
import sympy as sp

f = lambda x: 10 / (-x * np.sqrt(x))
a = 20
b = 5
n = 5

x = sp.symbols("x")
f_exact = 10 / (-x * sp.sqrt(x))
integral = sp.integrate(f_exact, (x, a, b))


def sum_rechtecke(f, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(0, n):
        xi = a + i * h
        res = res + f(xi + h / 2)
    return h * res


näherung = sum_rechtecke(f, a, b, n)
print("Rechteck: ", näherung)
result = (integral - näherung).evalf()
print(np.abs(result))


def sum_trapez(f, a, b, n):
    h = (b - a) / n
    res = 0
    k = (f(a) + f(b)) / 2
    for i in range(1, n):
        xi = a + i * h
        res = res + f(xi)
    return h * (k + res)


näherung = sum_trapez(f, a, b, n)
print("Trapez: ", näherung)
result = (integral - näherung).evalf()
print(np.abs(result))


def sum_simpsons(f, a, b, n):
    h = (b - a) / n
    res1 = 0
    res2 = 0
    for i in range(1, n):
        xi = a + i * h
        res1 = res1 + f(xi)

    for i in range(1, n + 1):
        x1_minus_1 = a + (i - 1) * h
        xi = a + i * h
        res2 = res2 + f((x1_minus_1 + xi) / 2)

    return (h / 3) * ((1 / 2) * f(a) + res1 + 2 * res2 + (1 / 2) * f(b))


näherung = sum_simpsons(f, a, b, n)
print("Simpsons: ", näherung)
result = (integral - näherung).evalf()
print(np.abs(result))
