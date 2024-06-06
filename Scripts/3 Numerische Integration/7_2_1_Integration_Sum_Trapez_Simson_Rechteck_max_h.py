import numpy as np
import sympy as sy

x, h = sy.symbols('x h')

'''INPUT'''
f = sy.sin(x)
a, b = 0.0, np.pi  #

err = 1e-3
'''INPUT'''

df = sy.diff(f, x)
print(f'f\'(x) = {df}')
df = sy.diff(df, x)
print(f'f\'\'(x) = {df}')
zweite_ableitung = sy.lambdify(x, df)
vierte_ableitung = sy.lambdify(x, sy.diff(f, x, 4))

max_2 = np.max(np.abs(zweite_ableitung(np.arange(a, b, 0.1))))
max_4 = np.max(np.abs(vierte_ableitung(np.arange(a, b, 0.1))))

trap = sy.Eq(h ** 2 / 12 * (b - a) * max_2 - 10 ** -3, 0)
recht = sy.Eq(h ** 2 / 24 * (b - a) * max_2 - 10 ** -3, 0)
simp = sy.Eq(h ** 4 / 2880 * (b - a) * max_4 - 10 ** -3, 0)

print('sum-Rechteck h <= ', sy.solve(recht))
print('sum-Trapez h <= ', sy.solve(trap))
print('sum-Simpson h <= ', sy.solve(simp))
