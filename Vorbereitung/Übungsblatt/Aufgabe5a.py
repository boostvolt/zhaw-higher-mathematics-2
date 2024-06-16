import matplotlib.pyplot as plt
import numpy as np
import sympy as sy

x = np.array([25, 35, 45, 55, 65], dtype=np.float64)  # Messwerte xi
y = np.array([47, 114, 223, 81, 20], dtype=np.float64)  # Messwerte yi


def f(x, a):
    return a[0] / ((((x**2) - a[1] ** 2) ** 2) + a[2] ** 2)


lam0 = np.array([10**8, 50, 600], dtype=np.float64)  # Startvektor für Iteration
a = sy.symbols("a:{n:d}".format(n=lam0.size))

tol = 1e-3  # Fehlertoleranz
max_iter = 30  # Maximale Iterationen

g = sy.Matrix(
    [y[k] - f(x[k], a) for k in range(x.shape[0])]
)  # Fehlerfunktion für alle (xi, yi)
Dg = g.jacobian(a)

g_lambda = sy.lambdify([a], g, "numpy")
Dg_lambda = sy.lambdify([a], Dg, "numpy")

k = 0
lam = np.copy(lam0)
increment = tol + 1
err_func = np.linalg.norm(g_lambda(lam)) ** 2

while increment > tol and k <= max_iter:
    # QR-Zerlegung von Dg(lam)
    [Q, R] = np.linalg.qr(Dg_lambda(lam))
    delta = np.linalg.solve(R, -Q.T @ g_lambda(lam)).flatten()
    # Achtung: flatten() braucht es, um aus dem Spaltenvektor delta wieder
    # eine "flachen" Vektor zu machen, da g hier nicht mit Spaltenvektoren als Input umgehen kann

    lam = lam + delta
    err_func = np.linalg.norm(g_lambda(lam)) ** 2
    increment = np.linalg.norm(delta)
    k = k + 1
    print("Iteration: ", k)
    print("lambda = ", lam)
    print("Inkrement = ", increment)
    print("Fehlerfunktional =", err_func)
    print()


plt.plot(x, y, "o")
x = np.linspace(20, 70, 100)
plt.plot(x, f(x, lam), "-")
plt.show()
