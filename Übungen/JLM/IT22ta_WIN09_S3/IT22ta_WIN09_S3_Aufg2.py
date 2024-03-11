import sympy as sp

x, y = sp.symbols("x y")
f1 = x**2 / 186**2 - y**2 / (300**2 - 186**2) - 1
f2 = (y - 500) ** 2 / 279**2 - (x - 300) ** 2 / (500**2 - 279**2) - 1
p1 = sp.plot_implicit(sp.Eq(f1, 0), (x, -2000, 2000), (y, -2000, 2000))
p2 = sp.plot_implicit(sp.Eq(f2, 0), (x, -2000, 2000), (y, -2000, 2000))
p1.append(p2[0])
p1.show()

# ------------------------------------------------------------------------------------------------------------------------

x0_array = [
    sp.Matrix([-190, 70]),
    sp.Matrix([-1280, 1620]),
    sp.Matrix([740, 910]),
    sp.Matrix([250, 215]),
]
epsilon = 1e-5
f = sp.Matrix([f1, f2])
Df = f.jacobian([x, y])

# Newton-Raphson-Verfahren
for x0 in x0_array:
    f0 = f.subs([(x, x0[0]), (y, x0[1])])
    while f0.norm(2) > epsilon:
        Df0 = Df.subs([(x, x0[0]), (y, x0[1])])
        delta = Df0.LUsolve(-f0)
        x0 = x0 + delta
        f0 = f.subs([(x, x0[0]), (y, x0[1])])
    print(f"x0: {x0.evalf()}")
