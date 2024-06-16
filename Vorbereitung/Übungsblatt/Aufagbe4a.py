import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

"""INPUT"""
x_sym = sp.symbols("x")
x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
y = np.array([76, 92, 106, 123, 137, 151, 179, 203, 227, 250, 281, 309])
funcs = np.array([x_sym**3, x_sym**2, x_sym**1, x_sym**0])
funcs2 = np.array([x_sym**2, x_sym**1, x_sym**0])
"""INPUT"""


def create_funcs_matrix(x, funcs, x_sym):
    n = len(x)
    m = len(funcs)
    A = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            A[i][j] = funcs[j].subs([(x_sym, x[i])])
    return A


def get_fx(lambdas, funcs, x):
    f = 0
    for lam, func in zip(lambdas, funcs):
        f += lam * func

    return sp.lambdify(x, f)


def normalgleichung(A, y):
    return np.linalg.solve(A.T @ A, A.T @ y)


def fehlerfunktionale(A, B, y, lambdas, lambdas2):
    Ef = np.linalg.norm(y - A @ lambdas, 2) ** 2
    Ef2 = np.linalg.norm(y - B @ lambdas2, 2) ** 2

    print(f"E(f)\t\t= {Ef}")
    print(f"E2(f)\t\t= {Ef2}")


if __name__ == "__main__":
    np.set_printoptions(suppress=True)
    A = create_funcs_matrix(x, funcs, x_sym)
    B = create_funcs_matrix(x, funcs2, x_sym)

    # Normalgleichung
    lambdas = normalgleichung(A, y)
    lambdas2 = normalgleichung(B, y)
    f = get_fx(lambdas, funcs, x_sym)
    f2 = get_fx(lambdas2, funcs2, x_sym)
    y = f(x)
    y2 = f2(x)
    # a)
    print(f"Normalgleichung: \t {lambdas} \n")
    print(f"Normalgleichung: \t {lambdas2} \n")

    # b)
    # Konditionen und Fehlerfunktionale
    fehlerfunktionale(A, B, y, lambdas, lambdas2)

    # plot
    plt.plot(x, y, "o", label="Daten")
    plt.plot(x, y, "-r", label="Normalgleichung a")
    plt.plot(x, y2, "--g", label="Normalgleichung b")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

"""
a)
Normalgleichung: 	 [6.21600622e-06 7.70562771e-03 1.18695749e+00 7.78021978e+01] 
Normalgleichung: 	 [8.73126873e-03 1.14375624e+00 7.81098901e+01] 

b)
E(f)		= 66.48351648351645
E2(f)		= 66.93106893106903

p1(t) liefert knapp das bessere Ergebnis, weil es das kleinste Fehlerquadrat ist.

##### Beides richtig #####
"""
