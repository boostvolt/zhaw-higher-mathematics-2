import numpy as np
import sympy as sp

x0 = sp.Matrix([1.5, 3, 2.5])

x1, x2, x3 = sp.symbols("x1 x2 x3")
X = sp.Matrix([x1, x2, x3])
x = sp.Matrix([1.5, 3, 2.5])

f1 = x1 + x2**2 - x3**2 - 13
f2 = sp.log(x2 / 4) + sp.exp(0.5 * x3 - 1) - 1  # error
f3 = (x2 - 3) ** 2 - x3**3 + 7

F = sp.Matrix([f1, f2, f3])
Df = F.jacobian(X)

Df0 = Df.subs([(x1, 1.5), (x2, 3), (x3, 2.5)])
f0 = F.subs([(x1, 1.5), (x2, 3), (x3, 2.5)])
# g = f(x0) + Df(x0) * (x-x0)
g = f0 + Df0 * (X - x)

print(f0)
print(Df0)
print(g)