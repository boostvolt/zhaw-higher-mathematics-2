import sympy as sp

x1, x2 = sp.symbols("x1 x2")

Df0 = sp.Matrix([[-18, -3.6],[-3.6, 9.72]])
f0 = sp.Matrix([1.42, 1.044])

print(sp.solve(Df0,f0))