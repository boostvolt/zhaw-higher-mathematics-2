import numpy as np
import sympy as sp
from matplotlib import pyplot as plt

data = np.array(
    [
        [1971, 2250.0],
        [1972, 2500.0],
        [1974, 5000.0],
        [1978, 29000.0],
        [1982, 120000.0],
        [1985, 275000.0],
        [1989, 1180000.0],
        [1989, 1180000.0],
        [1993, 3100000.0],
        [1997, 7500000.0],
        [1999, 24000000.0],
        [2000, 42000000.0],
        [2002, 220000000.0],
        [2003, 410000000.0],
    ]
)


x = data[:, 0]
y = data[:, 1]
log_y = np.log10(y)

lambda_fit = np.polyfit(x - 1970, log_y, 1)

plt.semilogy(x, y, "o", label="Daten")
plt.semilogy(x, 10 ** (lambda_fit[0] * (x - 1970) + lambda_fit[1]))
plt.show()


t = sp.symbols("t")
f = np.array([1, (t - 1970)])

A = np.zeros((14, 2))

for i in range(0, 14, 1):
    for j in range(0, 2, 1):
        A[i][j] = sp.sympify(f[j]).subs(t, x[i])


def a_qr(A, log_y):
    Q, R = np.linalg.qr(A)
    return np.linalg.solve(R, Q.T @ log_y)


lambda_ = a_qr(A, log_y)

print("Im jahr 2015: ", 10 ** (lambda_[0] + lambda_[1] * (2015 - 1970)))

# O_0 beschreibt den Startwert und O_1 beschreibt den Anstieg der Transistoren. Wenn O_1 ungefähr 0.5 ist, dann würde es dem Moore'schen Gesetz entsprechen.
