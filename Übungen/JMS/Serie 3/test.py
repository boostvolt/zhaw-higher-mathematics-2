import sympy as sp

x, y = sp.symbols('x y')
f1 = x**2/186**2 - y**2/(300**2 - 186**2) - 1
f2 = (y - 500)**2/279**2 - (x - 300)**2/(500**2 - 279**2) - 1

p1 = sp.plot_implicit(sp.Eq(f1, 0), (x, -2000, 2000), (y, -2000, 2000), show=False)
p2 = sp.plot_implicit(sp.Eq(f2, 0), (x, -2000, 2000), (y, -2000, 2000), show=False)

p1.extend(p2)
p1.show()