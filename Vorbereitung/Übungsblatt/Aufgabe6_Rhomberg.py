import numpy as np


def Tf(f, a, b, n, j):
    print("     Startwert a = " + str(a))
    print("       Endwert b = " + str(b))
    print("Anzahl Schritte n = " + str(n))

    """----------INPUT----------"""
    # Schritweite h definieren
    h = (b - a) / 2**j
    """----------INPUT----------"""

    print("  Schrittweite h = (b - a) / n = " + str(h))

    xi = np.array([a + i * h for i in range(1, n)], dtype=np.float64)

    print("xi = " + str(xi))

    T = h * ((f(a) + f(b)) / 2 + np.sum(f(xi)))

    print("T{}0 = h * ((f(a) + f(b)) / 2 + SUM(f(xi))) = {}\n".format(j, T))

    return T


def romberg_extrapolate(f, a, b, m):
    print("1. Berechne die Tj0 mit der Trapezregel:")
    print("----------------------------------------")
    T = np.zeros((m + 1, m + 1), dtype=np.float64)

    T[0:, 0] = [Tf(f, a, b, 2**j, j) for j in range(m + 1)]

    print("2. Berechne die Tjk aus den Tj0:")
    print("--------------------------------")
    for k in range(1, m + 1):
        for j in range(m + 1 - k):
            T[j, k] = (4**k * T[j + 1, k - 1] - T[j, k - 1]) / (4**k - 1)
            print(
                "T{}{} = (4^{} * T{}{} - T{}{}) / (4^{} - 1) = {}".format(
                    j, k, k, j + 1, k - 1, j, k - 1, k, T[j, k]
                )
            )

    print("\nTij = \n", T)
    return T[0, m]


"""----------INPUT----------"""


# Funktion definieren
def f(x):
    return 2 * np.exp(-(((x / 10) - 2) ** 4))


# Start-Intervall
a = 0
# End-Intervall
b = 40
# Anzahl Schritte
m = 3
# ACHTUNG eventuell Schrittweite h in Funktion Tf(f, a, b, n, j) auf Zeile 10 noch anpassen
"""----------INPUT----------"""
T = romberg_extrapolate(f, a, b, m)

print("\nIntegral mit Romberg-Extrapolation: ", T)
