import matplotlib.pyplot as plt
import numpy as np


# Lagrange-Interpolation
def IT22ta_WIN09_S5_Aufg2(x, y, xx):
    a = y
    h = np.zeros(x.size - 1)
    c = np.zeros_like(x)
    A = np.zeros((x.size - 2, x.size - 2))
    z = np.zeros(c.size - 2)
    b = np.zeros(x.size - 1)
    d = np.zeros(x.size - 1)
    yy = np.zeros(xx.size)
    print(yy)
    for i in range(0, h.size):
        h[i] = x[i + 1] - x[i]

    for i in range(0, x.size - 2):
        A[i, i] = 2 * (h[i] + h[i + 1])
        if i + 1 < x.size - 2:
            A[i + 1, i] = h[i + 1]
            A[i, i + 1] = h[i + 1]
        z[i] = (3 * ((y[i + 2] - y[i + 1]) / h[i + 1])) - (
            3 * ((y[i + 1] - y[i]) / h[i])
        )

    c[1:-1] = np.linalg.solve(A, z)

    for i in range(0, x.size - 1):
        b[i] = ((y[i + 1] - y[i]) / h[i]) - ((h[i]) / 3 * (c[i + 1] + 2 * c[i]))

    for i in range(0, x.size - 1):
        d[i] = (1 / (3 * h[i])) * (c[i + 1] - c[i])

    # Durchlaufen der Werte in xx
    for i in range(xx.size):
        # Durchlaufen der Stützstellen
        for j in range(x.size - 1):
            if x[j] <= xx[i] <= x[j + 1]:
                yy[i] = (
                    a[j]
                    + b[j] * (xx[i] - x[j])
                    + c[j] * ((xx[i] - x[j]) ** 2)
                    + d[j] * ((xx[i] - x[j]) ** 3)
                )
                break
    return yy


# Wird nur ausgeführt wenn explizit dieses Script ausgeführt wird.
if __name__ == "__main__":
    # Gegebene Werte
    x = np.array([4.0, 6.0, 8.0, 10.0])
    y = np.array([6.0, 3.0, 9.0, 0.0])
    xx = np.arange(4.0, 10.1, 0.1)
    yy = IT22ta_WIN09_S5_Aufg2(x, y, xx)

    plt.plot(xx, yy)
    plt.plot(x, y, marker="o", linewidth=0)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Serie 5 - Aufgabe 2")
    plt.legend(["S(x)"])
    plt.grid()
    plt.show()
