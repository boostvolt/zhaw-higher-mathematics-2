import sympy as sp

x1, x2, x3 = sp.symbols("x1 x2 x3", positive=True)

f1 = x1 + x2**2 - x3**2 - 13
f2 = sp.log(x2 / 4) + sp.exp(0.5 * x3 - 1) - 1
f3 = (x2 - 3) ** 2 - x3**3 + 7

F = sp.Matrix([f1, f2, f3])
x = sp.Matrix([x1, x2, x3])
x0 = sp.Matrix([1.5, 3, 2.5])

g = F.subs([(x1, 1.5), (x2, 3), (x3, 2.5)]) + F.jacobian([x1, x2, x3]).subs(
    [(x1, 1.5), (x2, 3), (x3, 2.5)]
) * (x - x0)

print(g)
