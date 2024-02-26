import sympy as sp

x, y, z = sp.symbols("x y z")
f1 = 5*x*y
f2 = (x**2)*(y**2) + x + 2*y

f = sp.Matrix([f1, f2])
X = sp.Matrix([x, y])
Df = f.jacobian(X)
Df0 = Df.subs([(x, 1), (y, 2)])
print(Df0)

f1 = sp.ln(x**2 + y**2) + z**2
f2 = sp.exp(y**2 + z**2) + x**2
f3 = (1/(z**2 + x**2)) + y**2

f = sp.Matrix([f1, f2, f3])
X = sp.Matrix([x, y, z])
Df = f.jacobian(X)
Df0 = Df.subs([(x, 1), (y, 2), (z,3)])
print(Df0)



