import sympy as sp

x1, x2, x3 = sp.symbols("x1 x2 x3")

f1 = x1 + x2**2 - x3**2 - 13
f2 = sp.ln(x2/4) + sp.exp(0.5*x3-1) - 1
f3 = (x2 - 3) ** 2 - x3 ** 3 + 7
