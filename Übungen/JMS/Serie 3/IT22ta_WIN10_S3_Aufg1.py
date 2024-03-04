from sympy import sympify, diff, Matrix, symbols, sqrt

x1, x2 = symbols("x1 x2")

def newtonverfahren_anzahl_iterationen(matrix, x_0, iterationen):
    x_prev = x_0.copy()

    for i in range(iterationen):
        Df = matrix.jacobian([x1, x2])

        delta = -Df.inv().subs(x_0) * matrix.subs(x_0)

        x_0 = {key: x_0[key] + delta[i] for i, key in enumerate(x_0)}

        f_norm = Matrix([val for val in matrix.subs(x_0)]).norm()
        x_norm = Matrix([x_0[key] - x_prev[key] for key in x_0.values()]).norm()

        print(f"Iteration {i+1}: x = {x_0}, ||f(x^(k))|| = {f_norm}, ||x(k) - x(k-1)|| = {x_norm}")

        x_prev = x_0.copy()

# Funktion definieren
f1 = "20 - 18 * x1 - 2 * x2**2"
f2 = "-4 * x2 * (x1 - x2**2)"

A = Matrix([sympify(f1), sympify(f2)])

# Wert für x_0 definieren
x_0 = {"x1": 1.1, "x2": 0.9}

newtonverfahren_anzahl_iterationen(A, x_0, 2)