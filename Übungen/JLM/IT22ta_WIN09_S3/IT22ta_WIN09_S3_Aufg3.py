import sympy as sp

x1, x2, x3 = sp.symbols("x1 x2 x3")
f1 = x1 + x2 ** 2 - x3 ** 2 - 13
f2 = sp.log(x2 / 4) + sp.exp(0.5 * x3 - 1) - 1
f3 = (x2 - 3) ** 2 - x3 ** 3 + 7

f = sp.Matrix([f1, f2, f3])
Df = f.jacobian([x1, x2, x3])

x0 = sp.Matrix([1.5, 3, 2.5])
print(f)
print(Df)

k = 0.5  # Dämfpungsfaktor
tolerance = 1e-5  # Toleranz
max_iterations = 100  # Maximale Anzahl an Iterationen


def damped_newton_method(f, Df, x0, k, tolerance, max_iterations):
    for i in range(max_iterations):
        f_val = f.subs([(x1, x0[0]), (x2, x0[1]), (x3, x0[2])]).evalf()
        Df_val = Df.inv().subs([(x1, x0[0]), (x2, x0[1]), (x3, x0[2])]).evalf()

        delta = Df_val @ -f_val
        x0 = x0 + k * delta

        print(f"Iteration {i}: x0 = {x0}")
        print(f"Norm of f(x0) = {f_val.norm(2)}")
        if f_val.norm(2) < tolerance:
            print(f"Convergence {x0} reached after {i} iterations.")
            return 0

    return "Maximum iterations reached. Consider adjusting parameters."

# Lösung mit dem gedämpften Newton-Verfahren
damped_newton_method(f, Df, x0, k, tolerance, max_iterations)
