import numpy as np
import scipy as sp

a = 20
b = 5
h = -3
exact_result = sp.integrate.quad(lambda v: 10 / (-v * (v**0.5)), 20, 5)
print(f"Exaktes Resultat: {exact_result[0]}")


def f(v):
    return -10 * (v ** (-3 / 2))


# Aufgabe a)


def sum_rechtecksregel():
    sum = 0

    for i in range(0, 5):
        sum += f(a + i * h + h / 2)

    Rf = h * sum
    abs_error = np.abs(Rf - exact_result[0])

    print(f"Summierte Rechecksregel: {Rf}")
    print(f"Absoluter Fehler Rechtecksregel: {abs_error}")


# Aufgabe b)


def sum_trapezregel():
    sum = 0

    for i in range(1, 5):
        sum += f(a + i * h)

    Tf = h * ((f(a) + f(b)) / 2 + sum)
    abs_error = np.abs(Tf - exact_result[0])

    print(f"Summierte Trapezregel: {Tf}")
    print(f"Absoluter Fehler Trapezregel: {abs_error}")


# Aufgabe c)


def sum_simpsonregel():
    sum1 = 0
    sum2 = 0

    for i in range(1, 5):
        sum1 += f(a + h * i)

    for i in range(1, 6):
        sum2 += f(((a + (i - 1) * h) + (a + i * h)) / 2)

    Sf = h / 3 * (1 / 2 * f(a) + sum1 + 2 * sum2 + 1 / 2 * f(b))
    abs_error = np.abs(Sf - exact_result[0])

    print(f"Summierte Simpsonregel: {Sf}")
    print(f"Absoluter Fehler Simpsonregel: {abs_error}")


sum_rechtecksregel()
sum_trapezregel()
sum_simpsonregel()

# Reihenfolge der Geanuigkeit der 3 verschiedenen Methoden
# 1. am genausten & 3. am ungenausten
#
# 1. Simpsonregel
# 2. Rechtecksregel
# 3. Trapezregel
