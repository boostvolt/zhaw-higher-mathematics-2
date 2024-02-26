import sympy as sp


def compute_jacobian(matrix, unbekannte):
    matrix = sp.Matrix([sp.sympify(expr) for expr in matrix])
    symbols = list(matrix.free_symbols)
    return matrix.jacobian(symbols).subs(unbekannte)


########################################################################################

# Matrix definieren
matrix = ["5 * x * y", "x**2 * y**2 + x + 2 * y"]

# Unbekannte definieren
unbekannte = {"x": 1, "y": 2}

print(compute_jacobian(matrix, unbekannte))
