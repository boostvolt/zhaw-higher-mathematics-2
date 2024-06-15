import sympy as sy
import numpy as np

x, a, b, c, d = sy.symbols('x a b c d')
''' INPUT '''
f = a + 2 * x + c * x ** 2 + 0.5 * x ** 3

# für integral
[a, b] = {0, np.pi}
''' INPUT '''

df = sy.diff(f, x)
dfl = sy.lambdify(x, df)
F = sy.integrate(f, x)

print('Function:' + str(f))
print('Ableitung:' + str(df))
print('Integral:' + str(F))

g = np.abs(df * x) / np.abs(f)  # Konditionszahl
print(sy.simplify(g))  # Vereinfacht

integral = sy.lambdify(x, F)
print('Integral nummerisch:', integral(b) - integral(a))
